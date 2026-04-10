# MSDS 620: AI II: Natural Language Processing

**Credits:** 3  
**Level:** graduate  
**Prerequisites:** MSDS 610

## Course Description
Natural language processing techniques and applications using modern AI approaches.

## Key Topics
- NLP
- Text processing
- Language models
- Sentiment analysis
- Named entity recognition

---

## Information Bank
*Research and supplementary materials for each key topic below.*

### NLP

Natural Language Processing (NLP) is a interdisciplinary field combining computer science, artificial intelligence, and linguistics that enables computers to understand, interpret, and generate human language in meaningful and useful ways. It bridges the gap between human communication and machine understanding, allowing software to process unstructured text and speech data at scale. NLP powers many of the AI-driven tools people interact with daily, from virtual assistants to translation services.

- **Tokenization** breaks raw text into smaller units (words, subwords, or sentences) that serve as the foundational input for all downstream NLP tasks.
- **Part-of-Speech (POS) Tagging** assigns grammatical labels (noun, verb, adjective, etc.) to each token, enabling syntactic analysis of sentences.
- **Dependency Parsing** analyzes sentence structure to identify grammatical relationships between words, revealing how subjects, objects, and modifiers connect.
- **Semantic Analysis** goes beyond syntax to interpret the meaning of text, resolving word sense ambiguity and understanding intent.
- **Text Classification** assigns predefined categories to documents or passages, used in spam detection, topic labeling, and content moderation.
- **Word Embeddings** (Word2Vec, GloVe, FastText) represent words as dense numerical vectors that capture semantic relationships, enabling mathematical operations on language.

**Practical Applications:** NLP is deployed in virtual assistants (Alexa, Siri, Google Assistant), machine translation (Google Translate), grammar-checking tools (Grammarly), chatbots, search engines, and clinical text mining in healthcare.

Sources: [IBM - What is NLP](https://www.ibm.com/think/topics/natural-language-processing), [AWS - NLP Explained](https://aws.amazon.com/what-is/nlp/), [GeeksforGeeks - NLP Overview](https://www.geeksforgeeks.org/nlp/natural-language-processing-overview/)

---

### Text processing

Text processing (also called text preprocessing) is the critical first stage in any NLP pipeline, where raw, unstructured text is cleaned, normalized, and transformed into a structured format suitable for analysis by machine learning models. Without proper text processing, models receive noisy input that degrades performance and accuracy. The quality of text preprocessing directly determines the effectiveness of all subsequent NLP tasks.

- **Tokenization** splits continuous text into discrete tokens (words, subwords, or characters). Word-level tokenization is most common, while subword tokenization (Byte-Pair Encoding, WordPiece) is used by modern transformer models to handle out-of-vocabulary words.
- **Stopword Removal** filters out high-frequency words ("the," "is," "and") that carry minimal semantic value, reducing dimensionality and focusing models on content-bearing terms.
- **Stemming** reduces words to their root form by stripping suffixes using rule-based algorithms like the Porter Stemmer or Snowball Stemmer. It is fast but may produce non-dictionary words (e.g., "studies" becomes "studi").
- **Lemmatization** reduces words to their dictionary base form (lemma) using vocabulary lookup and morphological analysis, always producing valid words (e.g., "better" becomes "good"). It is more accurate than stemming but computationally heavier.
- **Text Normalization** includes lowercasing, removing punctuation, expanding contractions, and correcting misspellings to standardize input data.
- **Vectorization** converts processed text into numerical representations using techniques such as Bag-of-Words (BoW), TF-IDF (Term Frequency-Inverse Document Frequency), or learned embeddings.

**Practical Applications:** Text processing pipelines are essential in search engines for query matching, in social media analytics for cleaning noisy user-generated content, and in document classification systems where consistent input formatting directly impacts model accuracy.

Sources: [IBM - Stemming and Lemmatization](https://www.ibm.com/think/topics/stemming-lemmatization), [GeeksforGeeks - Text Preprocessing](https://www.geeksforgeeks.org/nlp/text-preprocessing-for-nlp-tasks/), [DEV Community - Complete Guide to NLP Text Preprocessing](https://dev.to/themustaphatijani/the-complete-guide-to-nlp-text-preprocessing-tokenization-normalization-stemming-lemmatization-50ap)

---

### Language models

Language models are AI systems trained to understand and generate human language by learning statistical patterns and relationships from large corpora of text. Modern language models are built on the Transformer architecture, introduced in 2017, which uses a self-attention mechanism to process entire input sequences in parallel and capture long-range dependencies between words regardless of their distance in the text. These models have revolutionized NLP by enabling transfer learning, where a model pretrained on massive datasets can be fine-tuned for specific tasks with relatively small amounts of labeled data.

- **Transformer Architecture** replaces recurrent processing with multi-head self-attention, allowing the model to weigh the relevance of every word in a sequence simultaneously. This enables much faster training through parallelization and better handling of long-range context.
- **BERT (Bidirectional Encoder Representations from Transformers)**, released by Google in 2018, is an encoder-only model that reads text bidirectionally. It uses Masked Language Modeling (MLM) during pretraining, making it excellent for understanding tasks like question answering, NER, and text classification.
- **GPT (Generative Pre-trained Transformer)**, developed by OpenAI, is a decoder-only autoregressive model that generates text by predicting the next token. GPT models excel at text generation, summarization, and conversational AI.
- **Fine-Tuning and Transfer Learning** allow practitioners to adapt large pretrained models to domain-specific tasks (legal, medical, financial text) using smaller annotated datasets, drastically reducing training time and data requirements.
- **Attention Mechanisms** assign different weights to input tokens based on their relevance to the current prediction, enabling models to focus on the most informative parts of a sentence.
- **Large Language Models (LLMs)** such as GPT-4, Claude, and LLaMA scale transformer architectures to billions of parameters, achieving broad general-purpose language understanding and generation capabilities.

**Practical Applications:** Language models power conversational AI assistants, automated content generation, code completion tools, document summarization, and real-time translation systems used by millions of people daily.

Sources: [IBM - How BERT and GPT Change NLP](https://www.ibm.com/think/insights/how-bert-and-gpt-models-change-the-game-for-nlp), [Wikipedia - Transformer](https://en.wikipedia.org/wiki/Transformer_(deep_learning)), [John Snow Labs - Introduction to LLMs](https://www.johnsnowlabs.com/introduction-to-large-language-models-llms-an-overview-of-bert-gpt-and-other-popular-models/)

---

### Sentiment analysis

Sentiment analysis (also called opinion mining) is an NLP technique that systematically identifies, extracts, and categorizes the emotional tone, opinions, and attitudes expressed in text data. It classifies text as positive, negative, or neutral, and more advanced systems detect fine-grained emotions such as joy, anger, frustration, or surprise. Sentiment analysis enables organizations to understand public opinion at scale by processing thousands of reviews, social media posts, or survey responses automatically.

- **Rule-Based / Lexicon Approaches** use predefined dictionaries of words scored by sentiment polarity (e.g., VADER, SentiWordNet). They are fast and interpretable but struggle with context, negation, and sarcasm.
- **Machine Learning Approaches** train classifiers (Naive Bayes, Support Vector Machines, Random Forest) on labeled datasets of text with sentiment annotations. These models learn patterns from features like word frequencies and n-grams.
- **Deep Learning Approaches** use Recurrent Neural Networks (RNNs), Long Short-Term Memory (LSTM) networks, and Convolutional Neural Networks (CNNs) to learn sequential and contextual patterns in text without manual feature engineering.
- **Transformer-Based Models** such as fine-tuned BERT achieve state-of-the-art sentiment classification by leveraging bidirectional context understanding, significantly outperforming traditional methods on benchmark datasets.
- **Aspect-Based Sentiment Analysis (ABSA)** goes beyond document-level polarity to identify sentiment toward specific aspects or features of a product or service (e.g., "the battery life is great but the screen is dim").
- **Challenges** include detecting sarcasm and irony, handling negation ("not bad" is positive), domain-specific vocabulary, multilingual text, and distinguishing subjective opinions from objective statements.

**Practical Applications:** Businesses use sentiment analysis to monitor brand reputation on social media, analyze customer reviews for product improvement, assess financial news for stock market predictions, and gauge public opinion on political issues or policy changes.

Sources: [AWS - Sentiment Analysis Explained](https://aws.amazon.com/what-is/sentiment-analysis/), [ScienceDirect - NLP-Based Sentiment Analysis Review](https://www.sciencedirect.com/science/article/pii/S2949719124000074), [Sapien.io - Sentiment Analysis in NLP](https://www.sapien.io/blog/sentiment-analysis-in-nlp)

---

### Named entity recognition

Named Entity Recognition (NER) is a subtask of information extraction that seeks to locate and classify named entities in unstructured text into predefined categories such as persons (PER), organizations (ORG), locations (LOC), dates, monetary values, and other domain-specific types. NER serves as a foundational building block for higher-level NLP tasks by transforming raw text into structured, actionable data. It is one of the first steps in many information extraction pipelines, enabling systems to understand *who*, *what*, *where*, and *when* a text is about.

- **Rule-Based Systems** use hand-crafted grammatical rules, gazetteers (lists of known entities), and regular expressions to identify entities. They achieve high precision but require significant manual effort and have lower recall on unseen data.
- **Statistical and ML Models** such as Conditional Random Fields (CRFs) and Hidden Markov Models (HMMs) learn sequential labeling patterns from annotated training data, using engineered features like capitalization, word shape, and surrounding context.
- **Deep Learning Approaches** employ BiLSTM-CRF architectures and Transformer-based models (BERT, RoBERTa) to automatically learn contextual representations, achieving state-of-the-art performance. These models resolve ambiguity (e.g., "Apple" as company vs. fruit) through broader context understanding.
- **IOB Tagging Scheme** (Inside-Outside-Beginning) is the standard annotation format where each token is labeled as B-TYPE (beginning of entity), I-TYPE (inside entity), or O (outside any entity), enabling multi-token entity recognition.
- **Common Entity Categories** include Person, Organization, Location, Date/Time, Monetary Value, Percentage, and domain-specific types like Gene, Drug, or Legal Citation in specialized applications.
- **Key Challenges** include entity ambiguity, name variation ("USA" vs. "United States"), nested entities, low-resource languages, and domain adaptation where models trained on news text may underperform on medical or legal documents.

**Practical Applications:** NER is used in search engines for query understanding, in healthcare for extracting drug names and diagnoses from clinical notes, in finance for identifying companies and monetary figures in reports, and in legal tech for locating parties and dates in contracts.

Sources: [IBM - Named Entity Recognition](https://www.ibm.com/think/topics/named-entity-recognition), [DataCamp - What is NER](https://www.datacamp.com/blog/what-is-named-entity-recognition-ner), [Wikipedia - Named-entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)

---

