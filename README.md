# Critical Reasoner v2.0 - Advanced System Prompt

## Overview

This repository contains the system prompt for **Critical Reasoner v2.0**, an advanced AI persona designed for deep, skeptical critical analysis of news articles, online claims, and other textual content. It instructs a Large Language Model (LLM) to go beyond surface-level fact-checking, incorporating rigorous source assessment, bias detection, logical integrity checks, and a unique simulated investigative inquiry function with built-in self-correction.

The goal is to create an AI tool that can act as a sophisticated assistant for identifying potential disinformation, low-quality reporting, and manipulative narratives, providing users with a nuanced assessment of information credibility.

## Core Features & Capabilities

Critical Reasoner v2.0 is instructed to perform the following functions:

1.  **Claim Segmentation:** Breaks down input text into manageable, analyzable claims or argument sections.
2.  **Enhanced Fact Verification:**
    *   Checks claims against external information (via web search/RAG).
    *   **Crucially:** Assesses the reliability of *verifying sources* before accepting their information.
    *   Weights evidence based on source quality, requiring stronger corroboration for claims from unreliable sources.
3.  **Bias Detection:** Identifies loaded language, framing, omissions, and rhetorical strategies indicative of bias or manipulation.
4.  **Integrated Source Criticism:**
    *   Assesses the reputation, bias, transparency, and potential conflicts of interest of cited/implied sources.
    *   Explicitly links source quality to the credibility of the claims being made.
5.  **Logical Integrity Analysis:** Evaluates the soundness of arguments, flagging fallacies, contradictions, and unsupported conclusions.
6.  **Enhanced Cross-Consistency Check:**
    *   Compares claims across multiple related texts (if provided).
    *   Identifies potential "narrative alignment" among sources with shared biases, treating it with skepticism rather than as strong corroboration.
7.  **Simulated Investigative Inquiry (Conditional):**
    *   **Triggered by anomalies:** Activates if initial analysis reveals significant red flags (e.g., very low trust scores, contradictions, heavy reliance on poor sources).
    *   **Hypothesis-driven:** Formulates questions based on anomalies.
    *   **Targeted Information Seeking:** Uses web search to explore context, connections, counter-arguments, funding, etc.
    *   **Actively seeks diverse perspectives and counter-evidence.**
8.  **Mandatory Self-Correction Checkpoint:**
    *   Before outputting investigative findings, the AI internally reviews them against checks for evidence basis, assumptions, alternative explanations, bias, and appropriate language caution.
    *   Filters or refines findings based on this self-critique to mitigate over-interpretation or speculation.
9.  **Nuanced Scoring & Synthesis:** Provides trust scores (0-100) for claims, with justifications *heavily* weighted by evidence quality and source reliability.

## How It Works (Process Flow)

The prompt guides the LLM through a structured workflow:

1.  **Input & Segmentation:** Receives text and breaks it down.
2.  **Parallel Analysis:** Analyzes each segment for facts, bias, source quality, and logic.
3.  **Investigative Threshold Check:** Determines if anomalies warrant deeper investigation.
4.  **Simulated Investigation (If Triggered):**
    *   Generates hypotheses.
    *   Conducts targeted searches.
    *   Synthesizes findings.
    *   **Performs mandatory self-correction.**
5.  **Scoring & Output:** Assigns justified trust scores and formats the complete analysis, clearly separating core analysis from optional investigative findings.

## Output Format

The output is structured for clarity:

*   **Core Analysis:** Presented per segment, detailing the claim, fact-check results (with source assessment), bias indicators, source criticism (and its impact), logic evaluation, and a trust score with explicit rationale.
*   **Investigative Threads (Optional):** If an investigation was performed and passed self-correction, this section details the trigger, the question pursued, the cautiously worded findings (with sources and confidence level), and the impact on the overall analysis.

## Requirements

*   A capable Large Language Model (LLM).
*   Support for system prompts / custom instructions.
*   **Crucial:** Access to a web search function (`function_call`) or a robust, up-to-date Retrieval-Augmented Generation (RAG) system for fact-checking and investigation. Performance will heavily depend on the quality and reliability of this external information access.

## Limitations

*   **Information Source:** Analysis is based solely on publicly available information accessible via the LLM's tools (web search/RAG).
*   **No Definitive Labels:** Cannot definitively label content as "fake news." It assesses credibility indicators.
*   **Simulated Investigation:** The investigative capability is a simulation based on information retrieval and synthesis; it cannot perform real-world actions (interviews, private data access). Findings are plausible hypotheses, not established truths.
*   **AI Hallucinations:** Like all LLMs, the model might occasionally misunderstand instructions or generate incorrect information (hallucinate). The prompt's structure and self-correction aim to minimize this, but human oversight is recommended.
*   **Ethical Boundaries:** Operates based on its programmed ethical guidelines.

## Usage

Copy the contents of the `critical_reasoner_v2_prompt.txt` file (or the prompt text provided elsewhere in this repository) and paste it into the system prompt or custom instructions field of your chosen compatible LLM interface. Then, provide the news article or text you want analyzed as user input.

## Potential Applications

*   Media literacy education and training.
*   Assisting researchers in evaluating source credibility.
*   Tools for journalists or fact-checkers (as a preliminary analysis aid).
*   Content moderation support (identifying potentially problematic narratives).
*   Personal information verification assistant.

## Disclaimer

This prompt pushes the boundaries of LLM capabilities for critical analysis. While designed for rigor and skepticism, the outputs should always be critically reviewed by a human user. Do not rely solely on the AI's assessment for critical decisions. The effectiveness depends heavily on the underlying LLM's quality and the reliability of its information access tools.

## License

This project (the Critical Reasoner v2.0 system prompt) is licensed under the Apache License, Version 2.0.

Copyright 2025 Polyphron Digital

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

