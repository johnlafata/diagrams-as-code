import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

class aiml_platform_component:
  def __init__(self, component_name, component_type, description, cluster_membership, logo):
    self.component_name = component_name
    self.component_type = component_type
    self.description=description   
    self.cluster_membership = cluster_membership
    self.logo = logo

MODEL_CLUSTER = "model"
MODEL_DEVELOPMENT_CLUSTER = "model development"
KNOWLEDGE_CLUSTER = "knowledge"
FRONT_END_CLUSTER = "front end"

COMPONENT_TYPE_CUSTOM = "custom"
COMPONENT_TYPE_STORAGE = "storage"


# possible front end components
class front_end_components:
  chatbot = aiml_platform_component(
  component_name="chatbot\nGUI", 
  component_type=COMPONENT_TYPE_CUSTOM, 
  description="chatbot gui", 
  cluster_membership=FRONT_END_CLUSTER, 
  logo="logo-images/chatbot.png")  

  guardrails = aiml_platform_component(
  component_name="guardrails", 
  component_type=COMPONENT_TYPE_CUSTOM, 
  description="gaurdrails", 
  cluster_membership=FRONT_END_CLUSTER, 
  logo="logo-images/nemo-guardrails.png")  

  api_gateway = aiml_platform_component(
  component_name="api_gateway", 
  component_type=COMPONENT_TYPE_CUSTOM, 
  description="api_gateway", 
  cluster_membership=FRONT_END_CLUSTER, 
  logo="logo-images/gateway.png")
  
  def __init__(self):
    logging.debug("aiml_platform_component.front_end_components class created")

# possible LLM model components
class model_components:
  openai_llm = aiml_platform_component(
    component_name="OpenAI", 
    component_type=COMPONENT_TYPE_CUSTOM, 
    description="OpenAI", 
    cluster_membership=MODEL_CLUSTER, 
    logo="logo-images/openai-logo.png")  

  llama_llm = aiml_platform_component(
    component_name="llama", 
    component_type=COMPONENT_TYPE_CUSTOM, 
    description="llama 3.2\n from Meta", 
    cluster_membership=MODEL_CLUSTER, 
    logo="logo-images/llama-logo.png")  

  claude_llm = aiml_platform_component(
    component_name="Anthropic Claude", 
    component_type=COMPONENT_TYPE_CUSTOM, 
    description="Anthropic Claude", 
    cluster_membership=MODEL_CLUSTER, 
    logo="logo-images/claude-logo.png")

  qroq_llm = aiml_platform_component(
    component_name="Groq", 
    component_type=COMPONENT_TYPE_CUSTOM, 
    description="Groq", 
    cluster_membership=MODEL_CLUSTER, 
    logo="logo-images/groq-logo.png")

  deepseek_llm = aiml_platform_component(
    component_name="Deepseek", 
    component_type=COMPONENT_TYPE_CUSTOM, 
    description="Deepseek", 
    cluster_membership=MODEL_CLUSTER, 
    logo="logo-images/deepseek-logo.png")

  def __init__(self):
    logging.debug("aiml_platform_component.front_end_components class created")


# possible memory components
class knowledge_components:
  external_apis = aiml_platform_component(
    component_name="External tools/MCP", 
    component_type=COMPONENT_TYPE_CUSTOM, 
    description="External tools/MCP", 
    cluster_membership=KNOWLEDGE_CLUSTER, 
    logo="logo-images/api-integration-icon.png")

  user_index_dataset = aiml_platform_component(
    component_name="Embedded knowledge", 
    component_type=COMPONENT_TYPE_STORAGE, 
    description="Embedded knowledge", 
    cluster_membership=KNOWLEDGE_CLUSTER, 
    logo=None)
  

class model_development_components:
  external_apis = aiml_platform_component(
    component_name="External tools/MCP", 
    component_type=COMPONENT_TYPE_CUSTOM, 
    description="External tools/MCP", 
    cluster_membership=MODEL_DEVELOPMENT_CLUSTER, 
    logo="logo-images/api-integration-icon.png")

  filtered_dataset = aiml_platform_component(
    component_name="Filtered Dataset", 
    component_type=COMPONENT_TYPE_STORAGE, 
    description="Filtered Dataset", 
    cluster_membership=MODEL_DEVELOPMENT_CLUSTER, 
    logo=None)

  unfiltered_dataset = aiml_platform_component(
    component_name="Raw Dataset", 
    component_type=COMPONENT_TYPE_STORAGE, 
    description="Unfiltered Dataset", 
    cluster_membership=MODEL_DEVELOPMENT_CLUSTER, 
    logo=None)

