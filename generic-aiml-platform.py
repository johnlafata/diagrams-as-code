from platform_diagram.aiml_platform_class import AIMLPlatformDiagram
from platform_diagram.platform_components.aiml_component_class import aiml_platform_component

from platform_diagram.platform_components.aiml_component_class import front_end_components
from platform_diagram.platform_components.aiml_component_class import model_components
from platform_diagram.platform_components.aiml_component_class import knowledge_components
from platform_diagram.platform_components.aiml_component_class import model_development_components



if __name__ == "__main__":

  front_end_components = [front_end_components.chatbot, front_end_components.guardrails, front_end_components.api_gateway]
  model_components = [model_components.openai_llm, model_components.llama_llm, model_components.claude_llm, model_components.qroq_llm, model_components.deepseek_llm]
  knowledge_components = [knowledge_components.external_apis, knowledge_components.user_index_dataset]
  model_development_components = [model_development_components.external_apis, model_development_components.filtered_dataset, model_development_components.unfiltered_dataset]

  diagram_components = front_end_components + model_components + knowledge_components + model_development_components

  diagram = AIMLPlatformDiagram(filename="generic-aiml-platform", include_user=True, components=diagram_components)
  diagram.create_diagram()
