# PhD Shortlist Builder 

## Overview

This project builds an end-to-end system that generates a **ranked shortlist of PhD supervisors and programs** for a given student profile.
The system focuses on **data quality, relevance, and personalization**, ensuring that each recommendation is actionable and suitable for cold-email outreach.

---

## Key Features

   **Semantic Matching** using SentenceTransformers (not just keyword search)
   **Accurate PI Detection** using publication history and affiliation signals
   **Strict Country Filtering** (hard constraint enforcement)
   **Evidence-Based Recommendations** with paper titles and links
   **Personalized "why_match"** using LLMs
   **Tier Classification** (reach / target / safety)
   **Optimized Latency** with batch processing

---

## System Architecture

```
Student Profile
   ↓
Profile Parsing
   ↓
Paper Retrieval (Semantic Scholar API)
   ↓
Author Aggregation & Disambiguation
   ↓
Country Filtering (University Mapping)
   ↓
PI Detection (Heuristic + Temporal Signals)
   ↓
Eligibility Filtering (Regex-based NLP)
   ↓
Semantic Matching (Embeddings)
   ↓
Ranking Engine
   ↓
Tier Assignment
   ↓
Program Linking
   ↓
Batch LLM Personalization
   ↓
Final JSON Output
```

---

## Data Sources

* **Semantic Scholar API** – for papers, authors, and metadata
* **SentenceTransformers** – for semantic similarity
* **OpenAI API** – for generating personalized explanations

---

## How It Works

### 1. Input

A JSON student profile containing:

* Research interests
* Skills and experience
* Target countries (strict constraint)
* Resume text

---

### 2. Candidate Retrieval

* Papers are fetched using research keywords
* Authors are extracted from relevant papers

---

### 3. Author Disambiguation

* Authors are grouped using:

  * Name
  * Affiliation
* Reduces same-name collisions (e.g., "Wei Wang")

---

### 4. Filtering Layer

####  PI Detection

* Minimum publication threshold
* Career span analysis
* Affiliation-based filtering

####  Country Filtering

* Uses university-to-country mapping
* Ensures **100% adherence to target countries**

####  Eligibility Filtering

* Detects restrictions like:

  * "UK only"
  * "EU residents"
  * "Home fees only"

---

### 5. Ranking

Each candidate is scored using:

* Semantic similarity (student vs research work)
* Publication volume
* Recency

---

### 6. Tier Assignment

* **Reach** → High score, top institutions
* **Target** → Good match
* **Safety** → Lower threshold but relevant

---

### 7. Output Generation

Each recommendation includes:

* Name
* Institution
* Country
* Email (heuristic)
* Research focus
* Evidence (papers with links)
* Personalized `why_match`
* Tier classification
* Linked PhD programs

---

## Running the Project

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Add API keys

Update `config.py`:

```
OPENAI_API_KEY = "your-key"
```

### 3. Run the pipeline

```
python main.py
```

---

## Output

Generated file:

```
sample_output/output.json
```

Contains 50+ ranked PhD supervisor recommendations.

---

## Design Decisions

### 1. Focus on Data Quality over Quantity

Avoided noisy matches by:

* Strong filtering
* Semantic validation

---

### 2. Heuristic + ML Hybrid Approach

* Heuristics for filtering (fast, reliable)
* Embeddings for matching (accurate)

---

### 3. Latency Optimization

* Limited LLM calls to top candidates
* Batch processing

---

## Known Limitations

* Email extraction is heuristic-based
* Country detection relies on mapping (not exhaustive)
* Eligibility parsing uses rule-based patterns
* Author disambiguation may fail for identical affiliations

---

## Future Improvements

* Web scraping for faculty pages (better PI verification)
* Knowledge graph for author-institution linking
* Fine-tuned ranking model using feedback loop
* Real-time PhD position scraping

---

## Bonus: Feedback Loop Design

Future system improvements using outcome data:

* Increase ranking score for:

  * ADMIT / INTERVIEW / POSITIVE_REPLY
* Penalize:

  * WRONG_PERSON / NO_REPLY
* Train a learning-to-rank model using past outcomes

---

## Conclusion

This system prioritizes **precision, personalization, and real-world applicability**, ensuring that the generated shortlist is both **accurate and actionable** for PhD applications.

---
