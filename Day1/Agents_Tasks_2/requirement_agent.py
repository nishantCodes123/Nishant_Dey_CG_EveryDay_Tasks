from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm_config import chat_model

requirement_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a QA Requirement Analyst.
Analyze the provided system requirement and produce a structured breakdown covering:
1. Functional Requirements (User login, restaurant search, cart operations, coupon engine, delivery address selection, payment gateway, order placement & confirmation).
2. Missing or Ambiguous Requirements (e.g., taxes/delivery charges handling, multi-restaurant carts, coupon reusability, session timeout handling).
3. Field & Logic Validations (e.g., minimum cart value checks, address field constraints, payment gateway timeouts, invalid card/UPI formats).
4. Edge Cases & Boundary Conditions (e.g., cart value modified after coupon application, item stock depletion mid-checkout, network drops during payment webhook processing)."""
    ),
    (
        "human",
        "Requirement:\n{requirement}"
    )
])

requirement_chain = requirement_prompt | chat_model 
