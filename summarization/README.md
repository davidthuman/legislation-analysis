

# Summarization


## BillSum: A Corpus for Automatic Summarization of US Legislation

[BillSum GitHub](https://github.com/FiscalNote/BillSum)

Each US bill comes with a human-written summary from the Congressional Research Service (CRS).

The BillSum dataset contains a primary corpus of 22,218 US Congressional bills and reference summaries split into a train and a test set.

Document organization (location of a given section of text compared to the other sections, how sections are embedded other sections) should be an input into the model. Legislature is always formatted within a sections, subsections, and lists. Document position carries contextual information.

Position embeddings are used in BERT models to give the model access to positional information within the transformer model.

How do we deal with references to other laws?



## Summarization of Legal Texts with High Cohesion and Automatic Compression Rate

[The paper ](https://webdocs.cs.ualberta.ca/~miyoung2/Papers/LNAI_7856_Summarization_of_legal_texts_2013.pdf)