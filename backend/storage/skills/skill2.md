# Skill: Program Committee Review Comments

## Purpose

This skill guides the reviewer or AI model in reading an academic paper, considering the comments prepared for the authors, and producing confidential, rigorous, and well-justified comments for the program committee of a conference, journal, workshop, or symposium.

The goal is to support editorial and program committee decision-making by providing a concise but technically grounded assessment of the paper's scientific quality, contribution, methodological rigor, presentation quality, risks, limitations, and suitability for acceptance, rejection, or revision.

Unlike comments to authors, program committee comments may include confidential assessments, decision rationale, comparative judgment, concerns about fit, confidence, ethical issues, and recommendation-level reasoning that should not necessarily be shared directly with the authors.

## When to Use

Use this skill when you need to produce confidential review comments intended for a program committee, area chair, meta-reviewer, editor, or senior reviewer.

This skill is appropriate when:

- A full academic paper, short paper, journal article, workshop paper, demo paper, or technical report must be reviewed.
- Comments to the authors are already available and must be considered before writing committee-facing comments.
- The review must support a decision such as accept, weak accept, borderline, weak reject, reject, or request major revision.
- The reviewer must distinguish between feedback that helps authors improve the paper and confidential information that helps the committee make a decision.
- The paper belongs to Computer Science or related areas, including Software Engineering, Artificial Intelligence, Data Science, Information Systems, Human-Computer Interaction, Computer Networks, Databases, Security, Distributed Systems, and related fields.

Do not use this skill to produce author-facing feedback only. For author-facing feedback, use a dedicated paper review comments skill.

## Inputs

The reviewer or AI model should receive, whenever available:

1. **Paper content**
   - Title
   - Abstract
   - Introduction
   - Background or related work
   - Methodology
   - Experimental design
   - Results
   - Discussion
   - Limitations or threats to validity
   - Conclusion
   - References
   - Appendices, supplementary material, artifacts, datasets, or code links

2. **Comments to authors**
   - Major comments
   - Minor comments
   - Strengths
   - Weaknesses
   - Questions or requested clarifications
   - Suggestions for improvement

3. **Review context**
   - Venue, track, or journal scope
   - Review criteria
   - Page limits or formatting constraints
   - Artifact evaluation expectations
   - Ethical review expectations
   - Reproducibility requirements
   - Conflict-of-interest constraints

4. **Decision metadata, if available**
   - Preliminary recommendation
   - Reviewer confidence
   - Novelty score
   - Technical quality score
   - Presentation score
   - Relevance score
   - Artifact availability or reproducibility score

If some inputs are missing, explicitly state the limitation and avoid inventing unsupported information.

## Workflow

Follow this workflow when producing confidential comments for the program committee.

### 1. Read the paper structurally

Identify the paper's core elements:

- Research area and topic
- Problem statement
- Research objective
- Research questions or hypotheses
- Claimed contributions
- Proposed method, model, framework, tool, system, dataset, or empirical study
- Evaluation strategy
- Main findings
- Stated limitations
- Intended audience and venue fit

### 2. Read the comments to authors

Review the author-facing comments and extract:

- Main strengths already communicated to the authors
- Main weaknesses already communicated to the authors
- Major methodological concerns
- Minor presentation or clarity issues
- Open questions
- Suggestions for improvement
- Any potential mismatch between the severity of comments and the final recommendation

Do not simply repeat the author comments. Use them as evidence for a confidential decision-oriented assessment.

### 3. Assess scientific and technical contribution

Evaluate whether the paper makes a meaningful contribution to its field.

Consider:

- Is the problem relevant and well motivated?
- Is the contribution novel or incremental?
- Is the paper technically sound?
- Does it advance knowledge, practice, methodology, tools, datasets, systems, or empirical evidence?
- Is the contribution significant enough for the target venue?
- Are the claims proportional to the evidence presented?

### 4. Assess methodological rigor

Analyze the research design and evaluation quality.

Consider:

- Are the research questions clear and answerable?
- Is the methodology appropriate for the stated goals?
- Are datasets, benchmarks, participants, systems, or case studies adequately described?
- Are baselines, comparison methods, or control conditions appropriate?
- Are metrics justified and correctly interpreted?
- Are statistical analyses, qualitative procedures, or experimental protocols sound?
- Are threats to validity identified and discussed honestly?
- Are artifacts, code, datasets, prompts, models, or configurations sufficiently available for reproducibility?

### 5. Assess evidence and validity of conclusions

Determine whether the results support the paper's claims.

Consider:

- Are the results clearly presented?
- Are the findings convincing?
- Are alternative explanations considered?
- Are negative results or limitations discussed?
- Are conclusions overstated?
- Does the paper distinguish empirical evidence from speculation?

### 6. Assess presentation quality

Evaluate whether the paper is understandable and professionally written.

Consider:

- Logical organization
- Clarity of argumentation
- Quality of figures, tables, and examples
- Terminology consistency
- Adequacy of related work
- Quality of academic writing
- Reproducibility of descriptions
- Compliance with venue expectations

### 7. Identify decision-relevant strengths and weaknesses

Separate issues into decision-relevant categories:

- Strengths that support acceptance
- Weaknesses that support rejection or revision
- Borderline issues that require committee discussion
- Issues that are important but fixable
- Issues that are fundamental and not fixable within a revision cycle

### 8. Consider ethical, reproducibility, and community risks

Check whether the paper raises concerns that should be visible to the committee.

Examples include:

- Unclear data provenance
- Privacy or consent issues
- Inadequate treatment of human subjects
- Potential misuse of models, datasets, or tools
- Lack of transparency in AI-generated content or model usage
- Unavailable artifacts despite strong reproducibility claims
- Misleading claims or unsupported generalizations
- Citation omissions that distort novelty claims
- Conflicts of interest or possible overlap with prior work

Only raise such concerns when supported by the paper or review evidence.

### 9. Produce the confidential committee assessment

Write a concise, objective, and decision-oriented assessment that helps the committee understand:

- What the paper is about
- Why it may deserve acceptance or rejection
- Which issues are central to the decision
- Whether the author-facing comments are aligned with the recommendation
- Whether the paper is above, below, or near the venue threshold
- What should be discussed during the program committee meeting, if applicable

### 10. Assign or justify a recommendation

When required, provide a recommendation and justify it with evidence.

Possible recommendation labels may include:

- Strong accept
- Accept
- Weak accept
- Borderline
- Weak reject
- Reject
- Major revision
- Minor revision

Use the venue's official scale if provided.

## Review Dimensions

Use the following dimensions to structure the confidential evaluation.

### 1. Relevance and fit

Assess whether the paper fits the scope, audience, and expectations of the venue or track.

Questions to consider:

- Is the topic appropriate for the venue?
- Does it address a problem relevant to the community?
- Would the expected audience benefit from the contribution?

### 2. Originality and novelty

Assess whether the paper offers a new contribution.

Questions to consider:

- Is the work clearly differentiated from prior work?
- Are novelty claims accurate?
- Is the contribution substantial or mostly incremental?
- Does the related work adequately position the paper?

### 3. Technical soundness

Assess whether the work is technically correct and logically coherent.

Questions to consider:

- Are definitions, assumptions, algorithms, models, or procedures correct?
- Are experimental or analytical choices justified?
- Are claims consistent with the evidence?

### 4. Methodological rigor

Assess whether the research design is appropriate and sufficiently rigorous.

Questions to consider:

- Are research questions clear?
- Is the study design suitable?
- Are baselines fair?
- Are metrics meaningful?
- Are statistical or qualitative analyses appropriate?

### 5. Empirical evidence and results

Assess the strength of the evidence.

Questions to consider:

- Are the results convincing?
- Are tables and figures interpretable?
- Are findings discussed in relation to the research questions?
- Are conclusions supported by data?

### 6. Reproducibility and transparency

Assess whether the work can be inspected, replicated, or reused.

Questions to consider:

- Are datasets, code, prompts, parameters, models, and configurations described?
- Are artifacts available or promised?
- Are important implementation details missing?

### 7. Limitations and threats to validity

Assess whether the paper honestly discusses limitations.

Questions to consider:

- Are internal, external, construct, and conclusion validity threats addressed when relevant?
- Are limitations proportional to the claims?
- Are generalizations justified?

### 8. Ethical and societal considerations

Assess whether the paper handles ethical concerns responsibly.

Questions to consider:

- Are privacy, consent, fairness, security, or misuse risks considered when relevant?
- Are data collection and usage practices appropriate?
- Are AI-generated artifacts or automated decisions disclosed when relevant?

### 9. Presentation and clarity

Assess whether the paper communicates effectively.

Questions to consider:

- Is the paper well organized?
- Are the writing, figures, and tables clear?
- Are contributions easy to identify?
- Are terminology and notation consistent?

### 10. Overall recommendation

Assess whether the strengths outweigh the weaknesses for the target venue.

Questions to consider:

- Is the paper above the acceptance threshold?
- Are weaknesses fixable in a revision?
- Would acceptance benefit the community?
- Should the paper be discussed by the committee?

## Relationship to Author Comments

Program committee comments should be consistent with, but not identical to, comments to authors.

### Author comments should usually contain

- Constructive feedback
- Explanation of major and minor issues
- Questions for clarification
- Suggestions for improvement
- Professional and respectful critique

### Committee comments may additionally contain

- Confidential recommendation rationale
- Comparative assessment relative to venue standards
- Concerns about acceptance threshold
- Discussion points for the committee
- Reviewer confidence
- Ethical or reproducibility concerns
- Assessment of whether weaknesses are fixable
- Notes about disagreement between scores and written comments
- Concerns about novelty, overlap, or scope that require editorial judgment

### Avoid in committee comments

- Personal criticism of authors
- Unsupported suspicion
- Speculative accusations
- Overly casual language
- Dismissive tone
- Repetition of all author comments without decision-oriented synthesis
- Hidden arguments that directly contradict author comments without explanation

## Confidentiality Guidelines

Treat program committee comments as confidential.

Follow these rules:

1. Do not include content that should be directly shown to authors unless it is also appropriate for author-facing feedback.
2. Clearly separate confidential decision rationale from author-facing critique.
3. Do not reveal reviewer identity, private discussions, or committee deliberations.
4. Do not make unsupported allegations about plagiarism, misconduct, ethics violations, or conflicts of interest.
5. When raising sensitive concerns, describe the observable evidence and explain why it matters for the decision.
6. Use neutral, professional language even when recommending rejection.
7. Avoid emotional, sarcastic, or dismissive phrasing.
8. Do not overstate certainty when evidence is incomplete.
9. Explicitly mark uncertainty when the assessment depends on missing information.
10. Keep the comments useful for an area chair, meta-reviewer, editor, or program committee member.

## Output Structure

Use the following structure unless the venue provides a different required format.

```markdown
# Program Committee Comments

## Paper Summary for the Committee
Briefly summarize the paper's topic, objective, approach, and main contribution in 1-2 paragraphs.

## Overall Assessment
Provide a concise decision-oriented assessment of the paper's quality, significance, and fit for the venue.

## Main Strengths Relevant to the Decision
- Strength 1: Explain why it matters for acceptance or positive evaluation.
- Strength 2: Explain why it matters for acceptance or positive evaluation.
- Strength 3: Explain why it matters for acceptance or positive evaluation.

## Main Weaknesses Relevant to the Decision
- Weakness 1: Explain its severity and whether it is fixable.
- Weakness 2: Explain its severity and whether it is fixable.
- Weakness 3: Explain its severity and whether it is fixable.

## Relationship to the Comments for Authors
Explain whether the author-facing comments accurately communicate the main issues and whether the recommendation is aligned with those comments.

## Confidential Concerns for the Committee
Describe any concerns that are relevant to the committee but should not necessarily be included in author-facing comments, such as venue fit, novelty threshold, reproducibility risk, ethical issues, or confidence limitations.

## Recommendation
State the recommendation using the venue's scale, if available.

Recommended decision: <Strong Accept | Accept | Weak Accept | Borderline | Weak Reject | Reject | Major Revision | Minor Revision>

## Rationale for Recommendation
Justify the recommendation with evidence from the paper and the author comments. Explain why the strengths do or do not outweigh the weaknesses.

## Reviewer Confidence
Confidence: <High | Medium | Low>

Explain the confidence level, including any limitations caused by missing information, limited expertise, unclear artifacts, or ambiguous claims.

## Discussion Points for the Committee
- Point 1: A key issue that may require committee discussion.
- Point 2: A disagreement, uncertainty, or borderline factor.
- Point 3: A decision-relevant concern about novelty, rigor, fit, ethics, or reproducibility.
```

## Writing Guidelines

Write committee comments using the following principles.

### Be decision-oriented

Focus on what the committee needs to decide. Avoid excessive detail unless it affects the recommendation.

Weak phrasing:

> The paper has some issues.

Better phrasing:

> The paper addresses a relevant problem, but the evaluation lacks appropriate baselines, which makes the main performance claims insufficiently supported for acceptance at this venue.

### Be evidence-based

Support every major claim with evidence from the paper, author comments, or review criteria.

Weak phrasing:

> The contribution is weak.

Better phrasing:

> The contribution appears incremental because the proposed workflow is close to existing LLM-assisted review pipelines, and the paper does not clearly explain what technical capability is new beyond integrating existing components.

### Distinguish fixable issues from fundamental issues

Clarify whether weaknesses can be addressed through revision.

Examples of fixable issues:

- Missing explanations
- Unclear figures
- Incomplete related work discussion
- Minor methodological clarifications
- Formatting and organization problems

Examples of fundamental issues:

- Unsupported central claim
- Inadequate evaluation design
- Missing baseline required to validate the contribution
- Incorrect methodology
- Lack of novelty
- Serious ethical or reproducibility concerns

### Use a respectful and professional tone

Avoid language that is hostile, dismissive, or personal.

Weak phrasing:

> The authors clearly do not understand the area.

Better phrasing:

> The paper would benefit from a more precise positioning against prior work, as several closely related approaches are not discussed in sufficient depth.

### Be concise but complete

Program committee comments should usually be shorter than author comments but more explicit about decision rationale.

### Be transparent about uncertainty

If information is missing, state the uncertainty.

Example:

> My confidence is medium because the paper's empirical setup is not described in enough detail to fully assess the fairness of the comparison.

## Quality Checklist

Before finalizing the committee comments, verify that:

- [ ] The paper's objective and contribution are summarized accurately.
- [ ] The assessment considers both the paper and the comments to authors.
- [ ] The main strengths are clearly connected to the decision.
- [ ] The main weaknesses are clearly connected to the decision.
- [ ] The recommendation is justified with evidence.
- [ ] The comments distinguish fixable issues from fundamental issues.
- [ ] Confidential concerns are appropriate for the committee and not needlessly hidden from authors.
- [ ] The tone is professional, neutral, and respectful.
- [ ] Ethical, reproducibility, and validity concerns are mentioned when relevant.
- [ ] The review does not contain unsupported accusations or speculation.
- [ ] Reviewer confidence is stated and justified.
- [ ] The final recommendation is aligned with the written rationale.
- [ ] The review avoids copying author comments verbatim.
- [ ] The review is useful for an area chair, editor, or meta-reviewer.

## Example Output Template

```markdown
# Program Committee Comments

## Paper Summary for the Committee
This paper investigates <topic/problem> and proposes <method/tool/framework/approach>. The authors aim to <objective>, using <methodology/evaluation strategy>. The main claimed contribution is <contribution>.

## Overall Assessment
The paper addresses a <relevant/important/timely> problem and has strengths in <strengths>. However, its suitability for acceptance is limited by <main decision-relevant weaknesses>. Overall, the paper is <above/below/near> the expected threshold for this venue because <brief rationale>.

## Main Strengths Relevant to the Decision
- <Strength 1>: <Why this supports acceptance or a positive evaluation>.
- <Strength 2>: <Why this supports acceptance or a positive evaluation>.
- <Strength 3>: <Why this supports acceptance or a positive evaluation>.

## Main Weaknesses Relevant to the Decision
- <Weakness 1>: <Severity, evidence, and whether it is fixable>.
- <Weakness 2>: <Severity, evidence, and whether it is fixable>.
- <Weakness 3>: <Severity, evidence, and whether it is fixable>.

## Relationship to the Comments for Authors
The comments to authors <adequately/partially/inadequately> communicate the main technical concerns. The most decision-relevant issues are <issues>. The recommendation is <aligned/not fully aligned> with the author-facing comments because <explanation>.

## Confidential Concerns for the Committee
<Describe confidential concerns, if any. If there are none, state: "No additional confidential concerns beyond the issues already reflected in the review comments.">

## Recommendation
Recommended decision: <Strong Accept | Accept | Weak Accept | Borderline | Weak Reject | Reject | Major Revision | Minor Revision>

## Rationale for Recommendation
I recommend <decision> because <evidence-based rationale>. The paper's strengths include <strengths>, but the main concerns are <weaknesses>. These issues are <fixable/fundamental> and, in my assessment, <do/do not> prevent the paper from meeting the venue's acceptance threshold.

## Reviewer Confidence
Confidence: <High | Medium | Low>

My confidence is <confidence level> because <reason related to expertise, paper clarity, artifact availability, or evidence quality>.

## Discussion Points for the Committee
- <Discussion point 1>.
- <Discussion point 2>.
- <Discussion point 3>.
```

## Final Notes

The final committee comments should help the program committee make a fair, transparent, and evidence-based decision. The review should be technically rigorous, professionally written, and aligned with the paper's actual content and the comments prepared for the authors.
