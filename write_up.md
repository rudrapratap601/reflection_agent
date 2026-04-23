**Design Rationale: Daily Reflection Tree (Advanced Version)**

This system is a deterministic reflection agent designed to guide users through structured end-of-day thinking using a decision tree. Unlike generative systems, all logic, branching, and reflections are pre-defined. This ensures consistency, interpretability, and full control over the experience while still maintaining a human-like flow.

* * *

### 1\. Question Design

The questions are designed to feel natural for a tired user at the end of the day. Instead of abstract psychological language, they are grounded in real situations such as decision-making, effort, and attention.

Each axis follows a layered progression:

*   Observation → What happened
    
*   Interpretation → Why it happened
    
*   Reflection → What it means
    

Additionally, the system avoids repetition by ensuring that each question serves a distinct purpose. For example, instead of asking “where could you contribute more” multiple times, the system now separates:

*   Behaviour detection (Did you contribute?)
    
*   Cause diagnosis (Why didn’t you contribute?)
    

This shift makes the system feel more like a reasoning process rather than a survey.

* * *

### 2\. Axis Structure

The reflection is structured across three psychological axes:

*   **Axis 1 (Locus of Control)**  
    Identifies whether the user attributes outcomes to internal actions or external factors.
    
*   **Axis 2 (Contribution vs Entitlement)**  
    Examines whether the user focused on adding value or expecting outcomes.
    
*   **Axis 3 (Perspective Radius)**  
    Evaluates whether attention was self-centered or extended toward others.
    

Each axis builds on the previous one, creating a progressive shift:

Control → Contribution → Perspective

This sequencing mirrors how awareness typically expands in real reflection.

* * *

### 3\. Branching Logic

The system uses two types of deterministic branching:

1.  **Answer-based decisions**  
    Direct mapping from user choices to the next node.
    
2.  **State-based decisions (signals)**  
    Each answer updates internal counters (e.g., internal vs external, contribution vs entitlement).  
    The dominant state is then used to guide future questions.
    

Example:

*   After Axis 1, the system computes whether the user leans **internal, external, or mixed**
    
*   This determines whether Axis 2 begins with a strength-based or reflective question
    

This creates personalization without randomness.

* * *

### 4\. Behavioral Depth (Key Improvement)

A major improvement in this version is the introduction of **cause-based questioning**.

Instead of repeating similar questions, the system now separates:

*   Outcome → “What happened?”
    
*   Cause → “Why did it happen?”
    

For example:

*   If low contribution is detected, the system asks what prevented contribution (motivation, focus, awareness)
    

This transforms the system from a simple questionnaire into a lightweight behavioral analysis tool.

* * *

### 5\. Handling Ambiguity

Human behaviour is rarely binary. To reflect this, the system supports a **“mixed” state** when signals are evenly distributed.

Instead of forcing classification, reflections acknowledge this nuance:

*   Users may show both internal and external tendencies in the same day
    
*   The system highlights patterns without oversimplifying them
    

* * *

### 6\. Reflection Tone

The tone of reflections is intentionally:

*   Non-judgmental
    
*   Observational rather than prescriptive
    
*   Calm and neutral
    

The system avoids motivational or corrective language. The goal is to increase awareness, not to instruct or evaluate.

* * *

### 7\. Design Trade-offs

*   More branching improves personalization but increases structural complexity
    
*   Simpler flows are easier to maintain but reduce behavioral depth
    

This system balances both by:

*   Using deeper branching only where it adds insight (e.g., Axis 2 entitlement path)
    
*   Keeping other parts linear for flow consistency
    

* * *

### 8\. Possible Improvements

Given more time, the system could be extended by:

*   Adding deeper cause-analysis in Axis 3 (attention vs impact gap)
    
*   Introducing multiple reflection templates for variation
    
*   Tracking patterns across multiple days (long-term behavior trends)
    
*   Building a simple UI for smoother interaction
    

* * *

### Core Idea

The system transforms abstract psychological concepts into a structured, navigable experience.  
By combining deterministic logic with human-centered question design, it creates a reflection process that is both consistent and meaningful — without relying on generative AI.