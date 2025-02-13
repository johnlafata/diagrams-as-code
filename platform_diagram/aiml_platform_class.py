from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.c4 import SystemBoundary, Person, Relationship, System
from diagrams import Edge
from diagrams.programming.flowchart import StoredData, Database, Decision
from diagrams.generic.storage import Storage

from platform_diagram.platform_components.aiml_component_class import aiml_platform_component

# local helper function
def make_component(component_to_make):
  new_component = None
  # for component_to_make in component_list:
  if component_to_make.component_type.lower() == "custom":
    new_component = Custom(component_to_make.component_name, component_to_make.logo)
  elif component_to_make.component_type.lower() == "storage":
    new_component = Storage(component_to_make.component_name)
    # new_components.append(new_component)
  return new_component

class AIMLPlatformDiagram:

  front_end_components = []
  front_end_component_list = []
  knowledge_components = []
  knowledge_component_list = []
  model_components = []
  model_component_list = []
  model_development_components = []
  model_development_component_list = []

  def __init__(self, diagram_title="Platform Components", filename="aiml-platform", include_user=True, 
          components=list[aiml_platform_component]):
    self.graph_attr = {
      "fontsize": "24",
      "bgcolor": "white",
      "splines": "spline"
    }
    self.diagram_title = diagram_title
    self.filename = filename
    self.include_user = include_user
    self.components=components


  def create_diagram(self):
    with Diagram(
      show=False, 
      direction="TB", 
      filename=self.filename, 
      graph_attr=self.graph_attr
    ) as platform_diagram:

      for component in self.components:
        if isinstance(component, aiml_platform_component):
          if component.cluster_membership.lower()== "front end":
            self.front_end_components.append(component)
          if component.cluster_membership.lower() == "knowledge":
            self.knowledge_components.append(component)
          if component.cluster_membership.lower() == "model":
            self.model_components.append(component)
          if component.cluster_membership.lower() == "model development":
            self.model_development_components.append(component)
        else:
          print("component is not an instance of aiml_platform_component")  

      if self.include_user:
        user = Custom("User", "logo-images/computer-user.png")

      with Cluster(self.diagram_title, direction="TB"):
        with Cluster("Front End", direction="LR"):
          if self.front_end_components is not None:
            for front_end_component in self.front_end_components:
              self.front_end_component_list.append(make_component(front_end_component))  
            
        # This cluster is static and does not change - due to limitations of the diagram as code tool
        # a cluster cannot point to another cluster, hence the list to list error. You'll need to connect to an entity inside the cluster.
        # This is mentioned at the bottom of this page: https://diagrams.mingrammer.com/docs/guides/node#group-data-flo
        with Cluster("Compute and Reasoning"):
          agent_pool = Custom("Agents available", "logo-images/agent-logo2.webp")
          context = Custom("User Specific Context", "logo-images/memory-icon.png")

        with Cluster("Knowledge"):
          # to ensure that the fine tuning cluster connects to memory, this element needs to be here
          long_term_memory = Custom("Long-term embedded\n vector data", "logo-images/vector-database.png")
          if self.knowledge_components is not None:
            for knowledge_component in self.knowledge_components:
              self.knowledge_component_list.append(make_component(knowledge_component))  

        with Cluster("Models"):
          if self.model_components is not None:
            for model_component in self.model_components:
              self.model_component_list.append(make_component(model_component))  

        if self.model_development_components is not None and len(self.model_development_components) >0:
          with Cluster("Fine Tuning"):
            # always include a llama-index component to connect to the long term storage if we're including fine-tuning
            cc_llama_index = Custom("llama_index", "logo-images/llamaindex-logo.png")
            if self.model_development_components is not None:
              for model_development_component in self.model_development_components:
                self.model_development_component_list.append(make_component(model_development_component))  

      # typically there is a user that interacts with the platform, but it's optional
      if self.include_user:
        user >> platform_diagram
        user >> self.front_end_component_list

      # front end should always connect to the agent pool
      (self.front_end_component_list) >> agent_pool

      # knowledge and long term memory is available to the context
      (self.knowledge_component_list) >> context      
      long_term_memory >> context 

      # agents determine which model to use
      agent_pool >> (self.model_component_list)
      # when we're including fine-tuning in platform, always include llama-index to long-term memory 
      if self.model_development_components is not None and len(self.model_development_components) >0:
        cc_llama_index >> long_term_memory

