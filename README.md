# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
I'm going to choose what it is actually like to live in each of the residence halls on Brandeis' campus. This knowledge is valuable during the housing lottery, where you only have a 2 minute window to choose where you'll live the next school year and those you want to bring with you. It's hard to find because Brandeis staff aren't living there, the students are, so they are biased since they want people to live there. Student's will tell the truth, administrators won't.


---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | "A review of life in Rosie" | A student review of Rosenthal Quad covering the suite layout, common room dynamics with strangers, and maintenance issues like ants. | [thebrandeishoot.com](https://thebrandeishoot.com/2021/04/30/a-review-of-life-in-rosie/) |
| 2 | "A review of the Foster Mods living experience" | Detailed account of living in the senior "Mods," including physical decay, extreme temperature issues, and invasions of mice and ants. | [thebrandeishoot.com](https://thebrandeishoot.com/2021/03/05/a-review-of-the-foster-mods-living-experience/) |
| 3 | "East Quad: an attempt at an explanation" | Explores the confusing architecture of East Quad, the "dungeon-like" hallways, and the lack of water fountains on residential floors. | [thebrandeishoot.com](https://thebrandeishoot.com/2022/09/09/east-quad-an-attempt-at-an-explanation/) |
| 4 | "Is Brandeis better yet?" | Editorial highlighting maintenance failures across campus, including black mold in Ziv Quad, mice in North Quad, and sewage floods. | https://www.thejustice.org/article/2025/09/is-brandeis-better-yet |
| 5 | "Third spaces" | Focuses on first-year common rooms (Polaris Lounge, "Schlounge"), detailing issues with cleanliness, furniture, and smelly kitchens. | https://www.thejustice.org/article/2026/03/third-spaces |
| 6 | "Forum, Unfiltered — Julia Hardy" | A defense of East Quad (specifically Pomerantz-Rubenstein), arguing that rooms are spacious and bathroom crowds are minimal. | https://www.thejustice.org/article/2026/03/forum-unfiltered-julia-hardy |
| 7 | "Freshman Dorms : r/brandeis" | Student rankings of first-year buildings in North and Massell Quads, including details on room sizes, carpet vs. tile, and elevators. | [reddit.com/r/brandeis](https://www.reddit.com/r/brandeis/comments/1y/freshman_dorms/) |
| 8 | "Charles River Apartment Housing : r/brandeis" | Provides specifics on living in "Grad" housing, such as separate exterior entrances for roommates and cleaning responsibilities. | [reddit.com/r/brandeis](https://www.reddit.com/r/brandeis/comments/3mo/charles_river_apartment_housing/) |
| 9 | "Is the housing bad? : r/brandeis" | Peer reviews of Village A and North Quad (Gordon), noting amenities like A/C and the need for blackout curtains. | [reddit.com/r/brandeis](https://www.reddit.com/r/brandeis/comments/3mo/is_the_housing_bad/) |
| 10 | "Hoot Recommends: dorm essentials" | Practical student advice on surviving Brandeis housing, including the need for seat cushions, personal fans, and warm lighting. | [thebrandeishoot.com](https://thebrandeishoot.com/2023/09/29/hoot-recommends-dorm-essentials/) |

***

**Note on Source URLs:** The URLs for *The Justice* were identified directly within the source text. The URLs for *The Brandeis Hoot* and *Reddit* are reconstructed based on standard publication patterns or the domain names identified in the sources. You may wish to independently verify the exact web addresses for the Hoot and Reddit threads.

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size: 1000 characters**

**Overlap: 200 characters**

**Why these choices fit your documents:**

- For the Chunk Size: I choose this number because there are a couple of newletters and they follower a sort of "1 topic per paragraph" style, and 1000 characters seems about right to get 1 paragraph. Also, there are some reddit threads, and since they are short, 1000 characters should be able to contain a good amount of discourse about housing.
- For the Overlap: I choose this number because at the end of some paragraphs, there might be a transition in topic to make it flow into the next paragraph, so 200 characters should be able to help the model get a bit of surrounding context. 


**Final chunk count:**
67 chunks across 10 documents

**Five chunk examples:**

=== source: a-review-of-life-in-rosie ===
After you meander down the short hall from your bed or bathroom, you will find yourself in the common room. Since you can only select the three others who live on your side, this is where life becomes more complicated. If somehow you manage to have another friend, who also has a good number and gets the same floor in the same building as you then, you are home free, but life is never so kind to the typical introverted Brandeis student. So most likely you will find yourself in a living arrangement about as exciting as this year’s virtual Springfest. By that I, of course, mean that the four people living adjacent to you will most likely be strangers you haven’t an inkling of knowledge of.

=== source: a-review-of-life-in-rosie ===
The ants, which either come in biblical marches or are never there, become less relevant. There is still the issue of the generally ugly nature of the Rosie quad since it is simply paved and dull just like any business major, but the redeeming quality of Rosie is the common room! Rosie offers sophomores who do not want to walk from Grad and cannot get a room in Skyline a place to call their own! It is an apartment where they do not have to cook but can have a lounge and friends around them at all times. It is low maintenance and easy to decorate, but when the design flaw at the heart of it interferes with the student life within it, then it all comes crumbling down. Rosie has so much potential, it is lively and generally party central, but as time sees more unhappy sides of Rosie being forced to share a common room, the whole notion of suite style becomes unappealing. Nevertheless, if you can live with all of that, including the ants and ugly quad, I will let you in on a little secret

=== source: a-review-of-the-foster-mods-living-experience ===
The Mods were constructed in 1973, and it shows. Despite receiving a major renovation in 2014 that brought the furniture and carpeting to the current Brandeis standard, the place reeks of decay. Rusty hinges and broken cabinets abound, and the concrete steps literally crumble beneath your feet as you approach your own front door. These things are tolerable of course—even charming. Getting a utilities guy to come in and fix something isn’t particularly hard, though wait times can be long. Upon discovering that our six-person Mod only had two kitchen chairs, the utilities men kindly delivered some new ones (and patched up a set of cabinet doors too). They’ve come by to fix locks and plane down warped doors as well.

=== source: hoot-recomends-dorm-essentials ===
Calli: There are quite a few items in my dorm room that I could not live without; my fan, beanbag chair, the colorful decorations that remind me of home. However, the one item that stands out the most to me is my foam roller. That thing has been through it all with me yet it never fails to make me feel better. Even my dog sees it as the coolest (though forbidden) toy in existence. As a runner, having a roller is a staple to keeping myself feeling fresh. Despite this, you certainly do not need to be a runner to own a foam roller. Hiking across campus and perhaps up the Rabb steps on the daily makes every Brandeis student a perfect foam roller candidate in my eyes. I usually foam roll every night before bed and stretch to decompress. It’s a healthy habit to form as it can relieve most types of leg and back discomfort as long as you do it regularly. Especially considering how much the average student sits everyday, it is important to relieve muscle tension and also increase blood flow.

=== source: is-brandeis-better-yet ===
In the wake of losing the Lydian String Quartet and Musicology and Music Composition Ph.D. programs due to ongoing budget cuts, this Editorial Board understands that programs in the arts at Brandeis are typically the first to go. The University made that prospect abundantly clear when it silently eliminated Brandeis Arts Engagement, as well as terminated the contract of beloved Prof. Taylor Ackley (MUS) with no discretion to the public. This Board hopes that this reorganization plan will reinstate these lost initiatives and address the plethora of student critiques that have largely been sidelined.

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

### Retrieval Examples:

Test query: 'What is it like to live in the Foster Mods?'

-     --- Rank 1 | source: a-review-of-the-foster-mods-living-experience | distance: 0.7629 ---
     The Foster Mods represent a hamlet of privacy tucked into the armpit of Brandeis University—a verdant armpit brimming with rabbits and gravel and walled on three sides by a thin strand of trees. While these apartments lack the luxury of newer residence halls like Village and Ridgewood, the opportuni


- --- Rank 2 | source: a-review-of-the-foster-mods-living-experience | distance: 1.0718 ---
     The Mods serve their purpose. They aren’t nice, but they are out of the way. They are also less than a minute from the gym, so you can finally start working out. Those with a tight knit group of friends will absolutely love the experience. Choose the lower numbered Mods if you can! They sit atop the

- --- Rank 3 | source: a-review-of-the-foster-mods-living-experience | distance: 1.1128 ---
     The rustic flare of these apartments, while unsavory to some, is also their main draw. The Mods are out of the way, tucked in the proverbial woods. The Brandeis Police aren’t hanging out here. There aren’t anylowerclassmen around to screw up and summon a fleet of BEMCo cars. It is the most peaceful

- --- Rank 4 | source: a-review-of-the-foster-mods-living-experience | distance: 1.1923 ---
     The Mods were constructed in 1973, and it shows. Despite receiving a major renovation in 2014 that brought the furniture and carpeting to the current Brandeis standard, the place reeks of decay. Rusty hinges and broken cabinets abound, and the concrete steps literally crumble beneath your feet as yo

- --- Rank 5 | source: a-review-of-the-foster-mods-living-experience | distance: 1.2383 ---
     Practically speaking, the Mods offer the space for fun. The apartments aren’t stacked on top of each other like in Ridgewood, so stomp away! Though the kitchen and living rooms are technically two different rooms divided by a short staircase, a ledge is the only divider so the spaces breathe. Each l

These are good chunks because they explicitly walk about Foster Mods, a lot of which talk about their actual living experience. The top chunks are exactly from the document where someone is talking about their living experience, so that works well.

---

Test query: 'What are some halls with good hangout spots?'

- --- Rank 1 | source: third-spaces | distance: 0.9232 ---
     When asked the same question, Finkelstein said, “I mean in mine there’s not a lot there other than a fewcouches, so I’ve never really seen anyone hang out there. [In] the lounge under Scheffres I used to see people playing ping pong a lot but I think the table broke.”

     Brandeis’ common rooms have t

- --- Rank 2 | source: third-spaces | distance: 0.9874 ---
     The options for first-year dorms can vary from location to location, but one common factor is the presence of some type of lounge or common room. North Quad’s Scheffres Hall and Gordon Hall have the Polaris Lounge. Massell Quad’s Shapiro Hall also has the Shapiro Lounge, affectionately dubbed the “S

- --- Rank 3 | source: third-spaces | distance: 1.0354 ---
     Roy described the common room as a “third space,” a place other than home or work since those two placeshold too much weight, or in a university setting, outside of the dorms and the classrooms. Roy said, “I believe that Americans are kind of obsessed with ‘third places’ and that’s kind of why they

- --- Rank 4 | source: is-the-housing-bad | distance: 1.0798 ---
     - Mundane_Talk_1501: I’m currently in Massell and genuinely I think that it is not that bad, the buildings compared to North Quad is a bit older while North is more new. I like it since it near Sherman dining hall, but hate it that I have to go up the hill every morning other than that it’s actually

- --- Rank 5 | source: freshamn-dorms | distance: 1.0872 ---
     - Jsnake47: Freshmen are in Massell Quad and North Quad. The biggest thing to avoid is getting a forced triple—most of which are in Shapiro—or just the Shapiro basement at all. Besides that, Massell is much closer to a dining hall and the sciences whereas North is at the top of campus and is close t

The top 3 chunks are the most relevant, explicitly stating the names of some of the residence hall lounges and what people might in them. However, the last two chunks aren't really related, just talking primarily about freshman housing. 

---

Test query: 'Which halls has the best view of campus?'

- --- Rank 1 | source: third-spaces | distance: 0.7837 ---
     The options for first-year dorms can vary from location to location, but one common factor is the presence of some type of lounge or common room. North Quad’s Scheffres Hall and Gordon Hall have the Polaris Lounge. Massell Quad’s Shapiro Hall also has the Shapiro Lounge, affectionately dubbed the “S

- --- Rank 2 | source: is-the-housing-bad | distance: 0.8085 ---
     Away_Mycologist8366: Can anyone give any feedback on first year dorms at Brandeis/specific feedback on different Quads? Also is it true that Brandeis will not let you choose a roommate your first year?

     - ItsMrShroom: yes. The only thing you can choose is ur preference for a single, double, triple, 

- --- Rank 3 | source: freshamn-dorms | distance: 0.8344 ---
     - glitterxtimes: former freshman/rising sophomore here!!! i lived in renfield hall, which is in massell. north is the better quad all around, but my personal ranking would be reitman and cable (north), renfield, shapiro (both in massell), gordon and scheffres (north) and then deroy and usen (massell

- --- Rank 4 | source: freshamn-dorms | distance: 0.9318 ---
     - Jsnake47: Freshmen are in Massell Quad and North Quad. The biggest thing to avoid is getting a forced triple—most of which are in Shapiro—or just the Shapiro basement at all. Besides that, Massell is much closer to a dining hall and the sciences whereas North is at the top of campus and is close t

- --- Rank 5 | source: freshamn-dorms | distance: 0.9343 ---
     Such-Skirt2637: Okay so like how do freshman dorm assignments work? I filled out the housing app so everything is all ready (and i know my roommate is random). Do i get my roommate and dorm at once? Or do I get to pick which dorm building I want?

     - Jsnake47: It’s all random. You’ll know your roomma

**Model used:**

I used all-MiniLM-L6-v2. I did it because it was quick and also sounded like it was good for understanding the semantics of the chunks. This was important for me because users might urgently ask questions during their housing selection window, which is only ~2 mins. Also, the documents are very opinions based, so the model is good for the semantic embedding.

**Production tradeoff reflection:**

It looks like the model handled the blend of documents fine, and also it recognizes the jargon. However, it doesn't get the jargon that isn't explicitly named in the documents. (eg. Sherm (what we call it) instead of Sherman Dining Hall)

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System Response Examples**

Prompt: Which halls have some public lounges to hang out in?

Output: Scheffres Hall and Gordon Hall have the Polaris Lounge, and Shapiro Hall has the Shapiro Lounge (also known as the "Schlounge").

Sources:
- Third Spaces  (distance: 0.7377)
- Freshamn Dorms  (distance: 1.037)
- A Review Of The Foster Mods Living Experience (distance: 1.1108)

---

Prompt: What do people say about living in freshman housing?

Output: Moira Koleno '29 said it's nice to have a place to step out of her dorm room, but she wishes the common room in Renfield was separate from the kitchen because it's always smelly due to leftover food. Another student mentioned that their common room wasn't used much, with only a few couches and no activities.

Sources:
- Third Spaces  (distance: 0.9144)
- Charles River Apartment Housing  (distance: 0.9259)
- A Review Of The Foster Mods Living Experience  (distance: 0.9936)
- Freshamn Dorms  (distance: 0.9971)

---

**System prompt grounding instruction:**

System prompt I used:

`You are a housing advisor for Brandeis University students.
Answer questions using ONLY the excerpts provided below. Do not use any outside knowledge. 
If the answer cannot be found in the excerpts, say: "I don't have enough information in my sources to answer that."
Keep your answer concise and direct.`

I wanted to make it focus on being very direct, not require much reading for the output, and also not to give irrelevant / false information.

**How source attribution is surfaced in the response:**

The app has two different response interfaces: one for the actual response and another for the list of sources that it used. 

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What do people say about the air conditioning in Foster Mods? | It's very bipolar. It's either super hot or super cold | The Foster Mods lack air conditioning, and residents have to rely on other methods, such as using personal fans or devising optimal window configurations, to try to cool their rooms. | 10 | 9 |
| 2 | As a freshman who wants to do science coursework, which would be the best hall for me? | Any building in the Massell quad, since it is very close to the dining halls and the shapiro science center. | Based on the excerpts, Massell Quad is closer to the sciences and the main dining hall, so it would be a more convenient option for you. However, I don't have enough information in my sources to recommend a specific hall within Massell Quad as the "best" for science coursework. | 7 | 10 |
| 3 | Where should I live if I want to be around all of the parties? | You should go to Rosie, it's known as a party central due to the apartment style housing and being centered on campus. | I don't have enough information in my sources to answer that. | 8 | 0 |
| 4 | Heat makes my skin breakout, which halls have actually working AC? | Village, Skyline, and Gordan are known for having working air conditioning and good temperment. | I don't have enough information in my sources to answer that. | 8 | 0 |
| 5 | I have a mid housing number, and I really want a single even if it means living in any hall. Where might I still have a chance? | Chances are best in East Quad, Village, Foster Mods, or Rosie. | You might have a chance in East Quadrangle, as some of its doubles are being made available as singles for an extra price. | 9 | 7 |

**Retrieval quality:** Relevant / Partially relevant / Off-target  

Definitely Relevant, if available. I like that it doesn't try to make bad suggestions if it doesn't have it info.

**Response accuracy:** Accurate / Partially accurate / Inaccurate

If it has the info, it's pretty accurate.

---

## Failure Case Analysis



<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

I was doing the retrieval and embedding step after inspecting 5 random chunks, and while I was inspecting relevant chunks for some sample questions, I noticed that one of them was simply a header, with no useful information.

**What the system returned:**

This was the chunk when I asked about "What is it like living in Foster Mods", and you can see it gave no useful information.

A review of the Foster Mods living experience
Aaron LaFauci
March 5, 2021
Opinions

**Root cause (tied to a specific pipeline stage):**

It was because of the data cleaning stage, and I wasn't fully aware of how the recursive chunk splitting worked, specifically on how it uses new lines to determine where chunks are. 

**What you would change to fix it:**

I solved it by just removing it since the sample size was small (just 10 documents), even though I knew that it wouldn't work for a larger project. The issue was that the headers weren't always consistent so I wasn't sure how to approach it. It now was 67 chunks. In the future, I would standardize my sources instead of having a blend in the first place, or make a more robust data cleaning function.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

It made my work grounded so I wasn't constantly confusing myself on what I should be doing. I needed to keep track of what does what, since I wasn't very familiar.

**One way your implementation diverged from the spec, and why:**

I actually didn't deviate. But if I wanted to, I would probably change the k values to be more than 5, so maybe it would be able to look at more sources and give better answers / more diverse set of opinions.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI: I have a list of sources that I want to put into a markdown table, help me format it. Don't output anything except the table.*
- *What it produced:*
  -  | # | Source | Description | URL or location |
     |---|--------|-------------|-----------------|
     | 1 | "A review of life in Rosie" | A student review of Rosenthal Quad covering the suite layout, common room dynamics with strangers, and maintenance issues like ants. | [thebrandeishoot.com](https://thebrandeishoot.com/2021/04/30/a-review-of-life-in-rosie/) |
     | 2 | "A review of the Foster Mods living experience" | Detailed account of living in the senior "Mods," including physical decay, extreme temperature issues, and invasions of mice and ants. | [thebrandeishoot.com](https://thebrandeishoot.com/2021/03/05/a-review-of-the-foster-mods-living-experience/) |
     | 3 | "East Quad: an attempt at an explanation" | Explores the confusing architecture of East Quad, the "dungeon-like" hallways, and the lack of water fountains on residential floors. | [thebrandeishoot.com](https://thebrandeishoot.com/2022/09/09/east-quad-an-attempt-at-an-explanation/) |
     | 4 | "Is Brandeis better yet?" | Editorial highlighting maintenance failures across campus, including black mold in Ziv Quad, mice in North Quad, and sewage floods. | https://www.thejustice.org/article/2025/09/is-brandeis-better-yet |
     | 5 | "Third spaces" | Focuses on first-year common rooms (Polaris Lounge, "Schlounge"), detailing issues with cleanliness, furniture, and smelly kitchens. | https://www.thejustice.org/article/2026/03/third-spaces |
     | 6 | "Forum, Unfiltered — Julia Hardy" | A defense of East Quad (specifically Pomerantz-Rubenstein), arguing that rooms are spacious and bathroom crowds are minimal. | https://www.thejustice.org/article/2026/03/forum-unfiltered-julia-hardy |
     | 7 | "Freshman Dorms : r/brandeis" | Student rankings of first-year buildings in North and Massell Quads, including details on room sizes, carpet vs. tile, and elevators. | [reddit.com/r/brandeis](https://www.reddit.com/r/brandeis/comments/1y/freshman_dorms/) |
     | 8 | "Charles River Apartment Housing : r/brandeis" | Provides specifics on living in "Grad" housing, such as separate exterior entrances for roommates and cleaning responsibilities. | [reddit.com/r/brandeis](https://www.reddit.com/r/brandeis/comments/3mo/charles_river_apartment_housing/) |
     | 9 | "Is the housing bad? : r/brandeis" | Peer reviews of Village A and North Quad (Gordon), noting amenities like A/C and the need for blackout curtains. | [reddit.com/r/brandeis](https://www.reddit.com/r/brandeis/comments/3mo/is_the_housing_bad/) |
     | 10 | "Hoot Recommends: dorm essentials" | Practical student advice on surviving Brandeis housing, including the need for seat cushions, personal fans, and warm lighting. | [thebrandeishoot.com](https://thebrandeishoot.com/2023/09/29/hoot-recommends-dorm-essentials/) |

- *What I changed or overrode: When I was actually formatting the text, I cleaned the titles to be standardized*

**Instance 2**

- *What I gave the AI:*
  -"To get a sense of what I'm building, read Milestone 1 and 2 of @planning.md  I am building a RAG system for a Brandeis Housing Guide. I have 10 .md files in a  @documents/  folder. Based on my plan, write a Python script using LangChain's RecursiveCharacterTextSplitter to:

     - Load all files from the /docs folder.
     - Clean the text (remove any remaining HTML or boilerplate).
     - Split the text into chunks of 1,000 characters with an overlap of 200 characters.
     - Ensure each chunk's metadata includes the original filename (e.g., 'Rosie_Review') so I can cite it later."

- *What it produced:*
     - it wrote @ingest.py
- *What I changed or overrode:*
     - I changed the chunk size and overlap variables because they were incorrect. 
