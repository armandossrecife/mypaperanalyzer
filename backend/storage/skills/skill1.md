# Skill: Paper Review Comments

## Purpose

This skill guides the structured reading, critical analysis, and production of constructive technical comments for authors of academic papers. It is intended to support rigorous, respectful, and actionable peer-review-style feedback across Computer Science and related fields, including Software Engineering, Artificial Intelligence, Data Science, Information Systems, Human-Computer Interaction, Computer Networks, Security, and Systems.

The goal is not only to summarize the paper, but also to evaluate its scientific quality, technical contribution, methodological soundness, clarity, limitations, and readiness for publication or improvement.

## When to Use

Use this skill when asked to review, critique, assess, or provide comments to the authors of an academic paper, technical manuscript, preprint, conference submission, journal article, workshop paper, thesis-derived article, or research report.

This skill is especially useful when the expected output resembles:

- Comments to authors;
- Peer review feedback;
- Technical critique of a paper;
- Major and minor revision suggestions;
- Structured academic review;
- Strengths, weaknesses, and improvement recommendations;
- Scientific quality assessment;
- Methodology, results, and validity analysis.

Do not use this skill as a replacement for domain-expert judgment. Use it to organize, deepen, and improve the quality of review comments.

## Inputs

The reviewer should use one or more of the following inputs when available:

- Full paper text, PDF, LaTeX source, Markdown file, or manuscript draft;
- Paper title, abstract, introduction, methodology, results, discussion, and conclusion;
- Figures, tables, diagrams, algorithms, appendices, and supplementary material;
- Evaluation criteria, conference/journal guidelines, or review form;
- Target venue or research area;
- Specific review focus requested by the user, such as methodology, novelty, writing, reproducibility, experimental design, threats to validity, or technical contribution.

If some information is missing, explicitly state the limitation and avoid unsupported claims.

## Workflow

### 1. Read the Paper Structurally

Read the paper section by section. Identify the role of each section and how it contributes to the overall argument. Pay attention to the logical flow from problem definition to contribution, methodology, results, discussion, and conclusion.

Extract the following elements:

- Research topic and domain;
- Main objective;
- Research problem or gap;
- Research questions, hypotheses, or goals;
- Proposed solution, method, model, framework, tool, dataset, or theory;
- Claimed contributions;
- Evaluation strategy;
- Main findings;
- Limitations and threats to validity;
- Future work.

### 2. Identify the Core Contribution

Determine what the paper claims to contribute. Classify the contribution when possible, for example:

- New method, algorithm, architecture, framework, model, process, or tool;
- Empirical study, benchmark, dataset, survey, taxonomy, or replication;
- Theoretical model, conceptual framework, formalization, or design principle;
- Application of an existing technique to a new domain;
- Comparative evaluation of approaches;
- Case study or industrial experience report.

Assess whether the contribution is clearly stated, sufficiently novel, technically sound, and relevant to the target community.

### 3. Evaluate the Research Motivation and Problem Definition

Analyze whether the paper clearly explains:

- Why the problem matters;
- What gap exists in previous work;
- Who is affected by the problem;
- Why existing approaches are insufficient;
- What research question or objective the paper addresses;
- How the proposed work advances knowledge or practice.

Flag vague, overstated, or unsupported claims.

### 4. Analyze Related Work and Positioning

Evaluate whether the related work section:

- Covers relevant and recent literature;
- Includes foundational references;
- Compares the paper against close alternatives;
- Clearly identifies the gap addressed by the work;
- Avoids superficial citation listing;
- Explains how the paper differs from or improves upon prior work.

When appropriate, suggest missing lines of work or categories of literature, but avoid inventing references unless they are known and verifiable.

### 5. Assess Methodology and Technical Design

Evaluate whether the methodology is appropriate for the research objective. Consider:

- Clarity of the proposed method or approach;
- Adequacy of the study design;
- Suitability of datasets, corpora, benchmarks, participants, systems, or cases;
- Correctness of algorithms, models, pipelines, or procedures;
- Justification for parameter choices, baselines, metrics, and tools;
- Reproducibility of implementation and experimental setup;
- Alignment between research questions and evaluation methods.

Identify missing details that would prevent replication or weaken confidence in the results.

### 6. Evaluate Data, Experiments, and Metrics

For empirical, experimental, or computational papers, inspect:

- Dataset size, origin, quality, balance, and representativeness;
- Data preprocessing, annotation, cleaning, sampling, and splitting;
- Experimental protocol;
- Baselines and comparison groups;
- Evaluation metrics;
- Statistical tests or confidence intervals when relevant;
- Error analysis;
- Ablation studies or sensitivity analysis;
- Resource usage, latency, cost, scalability, or computational overhead when relevant.

Check whether the metrics actually support the paper's claims.

### 7. Examine Results and Interpretation

Assess whether the results are presented clearly and interpreted correctly. Verify whether:

- Tables and figures are readable and meaningful;
- Results answer the stated research questions;
- The discussion is consistent with the evidence;
- Claims are proportional to the findings;
- Negative, inconclusive, or unexpected results are discussed;
- Practical implications are explained;
- Limitations are acknowledged honestly.

Avoid overstating results beyond the evidence provided.

### 8. Review Validity, Limitations, and Reproducibility

Identify threats to validity or reliability, such as:

- Internal validity issues;
- External validity and generalizability limits;
- Construct validity problems;
- Conclusion validity concerns;
- Dataset bias;
- Small sample size;
- Weak baselines;
- Missing statistical analysis;
- Lack of replication package;
- Missing implementation details;
- Incomplete hyperparameter, prompt, tool, or environment description.

For software, AI, and data-intensive papers, check whether artifacts are available or sufficiently described, including source code, datasets, prompts, configurations, model versions, scripts, seeds, hardware, and dependency versions.

### 9. Assess Writing, Organization, and Presentation

Evaluate the manuscript's readability and academic presentation:

- Clarity of abstract and introduction;
- Logical section organization;
- Coherence between objectives, methods, results, and conclusions;
- Quality of figures, tables, captions, and diagrams;
- Definition of acronyms and technical terms;
- Grammar, style, and conciseness;
- Consistency of terminology;
- Adequacy of title and keywords;
- Compliance with formatting or venue guidelines.

Distinguish between scientific issues and presentation issues.

### 10. Produce Constructive Comments

Write comments that help authors improve the paper. Comments should be:

- Specific, not generic;
- Evidence-based, not speculative;
- Respectful, not aggressive;
- Actionable, not merely critical;
- Prioritized by importance;
- Connected to sections, claims, tables, figures, or methodological choices;
- Balanced between strengths and weaknesses.

Prefer comments such as:

> The evaluation would be stronger if the authors compared the proposed method against additional baselines that represent the current state of practice in the target domain.

Avoid comments such as:

> The evaluation is weak.

## Review Dimensions

Use the following dimensions to guide the critique.

### 1. Objective and Scope

Check whether the paper clearly defines its objective, scope, assumptions, and intended contribution.

### 2. Originality and Relevance

Assess whether the work is novel, relevant, and meaningful for the target research community.

### 3. Technical Soundness

Evaluate whether the proposed method, model, architecture, or analysis is technically correct and sufficiently detailed.

### 4. Methodological Rigor

Assess whether the study design, experimental protocol, data collection, and analysis methods are appropriate and justified.

### 5. Evidence and Results

Check whether the results support the claims and whether the analysis is complete, transparent, and convincing.

### 6. Comparison with Prior Work

Evaluate whether the paper positions itself adequately against related approaches, baselines, and existing evidence.

### 7. Reproducibility and Transparency

Assess whether another researcher could reproduce or validate the work based on the information provided.

### 8. Validity and Limitations

Identify whether the paper discusses threats to validity, limitations, assumptions, and boundary conditions.

### 9. Practical or Scientific Impact

Assess whether the work has clear implications for research, practice, industry, policy, education, or future studies.

### 10. Writing and Presentation Quality

Evaluate clarity, organization, language, formatting, visual elements, and overall readability.

## Output Structure

The final review comments should be organized using the following structure unless the user requests a different format.

### 1. Summary of the Paper

Briefly summarize the paper in one to three paragraphs. Include:

- Research problem;
- Proposed solution or approach;
- Methodology or evaluation strategy;
- Main results;
- Claimed contributions.

The summary should be descriptive and neutral.

### 2. Overall Assessment

Provide a concise overall assessment of the paper's quality, contribution, and main areas for improvement. Avoid assigning a recommendation unless the user or review form explicitly asks for one.

### 3. Strengths

List the main strengths of the paper. Each strength should be specific and justified.

Examples:

- The paper addresses a relevant and timely problem.
- The proposed method is clearly motivated by limitations in existing approaches.
- The evaluation uses appropriate metrics for the stated research questions.
- The paper provides useful implementation or deployment insights.

### 4. Major Comments

List the most important issues that affect the paper's scientific contribution, validity, technical soundness, or interpretability.

Major comments may address:

- Unclear research problem;
- Weak novelty or contribution;
- Inadequate methodology;
- Missing baselines;
- Insufficient dataset or sample size;
- Unsupported claims;
- Lack of statistical analysis;
- Missing threats to validity;
- Poor reproducibility;
- Misalignment between objectives and results.

Each major comment should include:

1. The issue;
2. Why it matters;
3. A concrete suggestion for improvement.

### 5. Minor Comments

List smaller issues that do not fundamentally undermine the paper but should be corrected or improved.

Minor comments may address:

- Typos, grammar, or wording;
- Formatting problems;
- Missing definitions;
- Unclear captions;
- Inconsistent terminology;
- Minor citation issues;
- Small improvements to figures, tables, or examples.

### 6. Suggested Improvements

Provide practical, prioritized recommendations. Suggestions should be objective and feasible.

Examples:

- Add a clearer statement of the research questions at the end of the introduction.
- Include a comparison with additional baselines.
- Expand the dataset description and clarify the sampling strategy.
- Add an ablation study to isolate the contribution of each component.
- Provide a replication package with code, data, prompts, and configuration files.
- Add a threats-to-validity section.

### 7. Questions for the Authors

Include questions that authors should answer to clarify the work. Questions should be technical, specific, and useful.

Examples:

- How were the hyperparameters selected?
- Why were these baselines chosen instead of more recent alternatives?
- How sensitive are the results to dataset size or sampling strategy?
- Can the proposed method generalize to other domains or datasets?
- Are the code, data, prompts, or experimental scripts available for replication?

### 8. Final Recommendation to Authors

End with a professional closing paragraph summarizing the most important revisions needed. Keep the tone constructive and respectful.

## Writing Guidelines

Follow these writing principles:

- Use a professional, academic, and respectful tone.
- Be direct but constructive.
- Focus on improving the paper, not criticizing the authors personally.
- Separate evidence-based critique from interpretation.
- Avoid vague statements such as “the paper is unclear” without explaining where and why.
- Avoid exaggerated claims such as “the work has no value.”
- Avoid rewriting the entire paper for the authors.
- Prefer actionable recommendations.
- Prioritize scientific and technical issues over stylistic issues.
- Use section, table, figure, or page references when available.
- Maintain consistency between the summary, strengths, weaknesses, and recommendations.
- Do not invent missing information. If the paper does not provide enough detail, state that explicitly.

## Quality Checklist

Before finalizing the review, verify that the comments satisfy the following checklist.

### Understanding

- [ ] The paper's topic and objective are correctly identified.
- [ ] The proposed contribution is clearly summarized.
- [ ] The methodology and evaluation are described accurately.
- [ ] The main results are represented fairly.

### Critical Analysis

- [ ] Strengths are specific and justified.
- [ ] Major weaknesses are clearly explained.
- [ ] Minor issues are separated from major issues.
- [ ] Methodological concerns are connected to validity or interpretation.
- [ ] Claims are checked against the evidence presented in the paper.

### Constructiveness

- [ ] Each major criticism includes a concrete suggestion.
- [ ] The tone is respectful and professional.
- [ ] Comments are actionable and useful to the authors.
- [ ] The review avoids vague or unsupported criticism.

### Reproducibility and Validity

- [ ] The review checks whether data, code, methods, and parameters are sufficiently described.
- [ ] Threats to validity or limitations are considered.
- [ ] The adequacy of baselines, metrics, and evaluation design is assessed.

### Presentation

- [ ] Writing quality, organization, figures, tables, and terminology are assessed.
- [ ] The final review is well-structured and easy to follow.
- [ ] The review does not include unnecessary repetition.

## Example Output Template

Use the following template when producing comments to authors.

```markdown
# Comments to Authors

## 1. Summary of the Paper

[Provide a concise and neutral summary of the paper. Mention the research problem, proposed approach, methodology, evaluation, and main findings.]

## 2. Overall Assessment

[Provide a balanced overall assessment of the paper's contribution, technical quality, clarity, and main areas requiring improvement.]

## 3. Strengths

- [Strength 1: Explain why this is a strength.]
- [Strength 2: Explain why this is a strength.]
- [Strength 3: Explain why this is a strength.]

## 4. Major Comments

### Major Comment 1: [Short title]

**Issue:** [Describe the main issue clearly.]

**Why it matters:** [Explain how this affects the paper's validity, contribution, reproducibility, or interpretation.]

**Suggestion:** [Provide a concrete and actionable recommendation.]

### Major Comment 2: [Short title]

**Issue:** [Describe the issue.]

**Why it matters:** [Explain the impact.]

**Suggestion:** [Recommend how the authors can address it.]

## 5. Minor Comments

- [Minor comment 1.]
- [Minor comment 2.]
- [Minor comment 3.]

## 6. Suggested Improvements

- [Improvement 1.]
- [Improvement 2.]
- [Improvement 3.]

## 7. Questions for the Authors

- [Question 1.]
- [Question 2.]
- [Question 3.]

## 8. Final Recommendation to Authors

[Close with a concise, respectful paragraph summarizing the most important actions the authors should take to improve the manuscript.]
```

## Additional Guidance for Computer Science Papers

When reviewing Computer Science papers, also consider the following domain-specific aspects.

### Software Engineering Papers

- Are research questions explicitly stated?
- Is the study design appropriate, such as case study, controlled experiment, survey, mining software repositories, or design science?
- Are projects, repositories, participants, issues, commits, or artifacts described adequately?
- Are threats to validity discussed using categories such as construct, internal, external, and conclusion validity?
- Are tools, scripts, datasets, and replication packages available?

### Artificial Intelligence and Machine Learning Papers

- Are datasets, preprocessing steps, prompts, model versions, and training or inference configurations described?
- Are baselines strong and current?
- Are metrics appropriate for the task?
- Are statistical significance, uncertainty, or variance reported when necessary?
- Are ablations or error analyses included?
- Are ethical risks, bias, privacy, and misuse considerations addressed when relevant?

### Systems and Infrastructure Papers

- Are workload assumptions realistic?
- Are scalability, latency, throughput, reliability, and cost evaluated?
- Is the experimental environment described, including hardware, software versions, and deployment settings?
- Are comparisons fair and reproducible?

### Data Science and Information Retrieval Papers

- Are data sources and collection methods transparent?
- Are retrieval, ranking, relevance, and evaluation protocols clearly defined?
- Are metrics such as precision, recall, F1-score, MAP, MRR, NDCG, faithfulness, or relevance used appropriately?
- Is there qualitative analysis of failure cases or errors?

## Review Ethics

A good review should be fair, confidential when applicable, and focused on scientific improvement. Do not include personal attacks, discriminatory language, or unsupported accusations. If ethical concerns are identified, describe them clearly and professionally, focusing on the manuscript and the evidence available.
