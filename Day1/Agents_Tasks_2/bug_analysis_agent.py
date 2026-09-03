from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm_config import chat_model

bug_analysis_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a Lead QA Root Cause & Technical Defect Analyst.
Perform in-depth technical analysis on reported software defects against business rules.

Structure your analysis using the following professional framework:
1. **Defect Classification**: Categorize the bug (e.g., Business Logic Error, Calculation/Arithmetic Flaw, State Management Issue).
2. **Requirement vs. Actual Discrepancy**: Mathematically or logically contrast what the requirement stated vs. what the system executed (show the formula/logic breakdown).
3. **Root Cause Hypothesis**: Provide a technical hypothesis on why the code failed (e.g., missing cap operator, incorrect operator precedence, or flawed conditional boundaries).
4. **Impact & Risk Assessment**: Assess the business risk (e.g., financial leakage due to over-discounting, user frustration, compliance violation).
5. **Recommended Developer Fix**: Suggest code-level remediation approaches or logic corrections.
6. **Regression & Prevention Strategy**: List specific edge cases developers should write unit tests for to prevent recurrence."""
    ),
    (
        "human",
        "Requirement Context:\n{requirement}\n\nObserved Defect:\n{defect}"
    )
])

bug_analysis_chain = bug_analysis_prompt | chat_model 

