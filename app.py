import os
from groq import Groq
from dotenv import load_dotenv
import gradio as gr
from retrieve import load_vector_store, retrieve

load_dotenv()

GROQ_MODEL = "llama-3.3-70b-versatile"

groq_client = Groq(api_key=os.environ["GROQ_API_KEY"])
collection, embed_model = load_vector_store()

SYSTEM_PROMPT = """You are a housing advisor for Brandeis University students.
Answer questions using ONLY the excerpts provided below. Do not use any outside knowledge.
If the answer cannot be found in the excerpts, say: "I don't have enough information in my sources to answer that."
Keep your answer concise and direct."""

def format_source_name(slug: str) -> str:
    """Convert a filename slug to a readable title, e.g. 'a-review-of-life-in-rosie' → 'A Review of Life in Rosie'."""
    return slug.replace("-", " ").title()


def answer_question(question: str):
    if not question.strip():
        return "", ""

    hits = retrieve(question, collection, embed_model, k=5)

    context_blocks = []
    for i, hit in enumerate(hits, 1):
        source = format_source_name(hit["source"])
        context_blocks.append(f"[{i}] Source: {source}\n{hit['text']}")
    context = "\n\n---\n\n".join(context_blocks)

    user_message = f"Context excerpts:\n\n{context}\n\nQuestion: {question}"

    response = groq_client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.2,
    )

    answer = response.choices[0].message.content.strip()

    # Deduplicate sources while preserving rank order
    seen = set()
    unique_sources = []
    for hit in hits:
        name = format_source_name(hit["source"])
        if name not in seen:
            seen.add(name)
            unique_sources.append(f"• {name}  (distance: {hit['distance']})")
    sources_text = "\n".join(unique_sources)

    return answer, sources_text


with gr.Blocks(title="Brandeis Housing Guide") as demo:
    gr.Markdown("# 🏠 Brandeis Unofficial Housing Guide")
    gr.Markdown("Ask anything about dorms, quads, amenities, or student experiences — answers come directly from student reviews and Reddit threads.")

    with gr.Row():
        question_box = gr.Textbox(
            label="Your question",
            placeholder="e.g. What is it like to live in the Foster Mods?",
            lines=2,
        )

    ask_btn = gr.Button("Ask", variant="primary")

    with gr.Row():
        answer_box = gr.Textbox(label="Answer", lines=8, interactive=False)

    with gr.Row():
        sources_box = gr.Textbox(label="Sources used", lines=6, interactive=False)

    ask_btn.click(fn=answer_question, inputs=question_box, outputs=[answer_box, sources_box])
    question_box.submit(fn=answer_question, inputs=question_box, outputs=[answer_box, sources_box])

if __name__ == "__main__":
    demo.launch()
