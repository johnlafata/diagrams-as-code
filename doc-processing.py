from platform_diagram.aiml_platform_class import AIMLPlatformDiagram
from platform_diagram.platform_components.aiml_component_class import aiml_platform_component

from platform_diagram.platform_components.aiml_component_class import front_end_components
from platform_diagram.platform_components.aiml_component_class import model_components
from platform_diagram.platform_components.aiml_component_class import knowledge_components



if __name__ == "__main__":

  front_end_components = [front_end_components.chatbot]

  embedding_model = aiml_platform_component(
    component_name="embedding model", 
    component_type="custom", 
    description="openai text-embedding-ada-002", 
    cluster_membership="model", 
    logo="logo-images/openai-logo.png")  

  model_components = [embedding_model]  

  knowledge_components = [knowledge_components.external_apis, knowledge_components.user_index_dataset]
  diagram_components = front_end_components + model_components + knowledge_components 

  diagram = AIMLPlatformDiagram(filename="doc-processing", diagram_title="Document Processing Application" ,include_user=True, components=diagram_components)
  diagram.create_diagram()
