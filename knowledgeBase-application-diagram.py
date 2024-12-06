## best example: 
## https://diagrams.mingrammer.com/docs/nodes/c4

from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.c4 import SystemBoundary, Person, Relationship, System
from diagrams import Edge
from diagrams.programming.flowchart import StoredData, Database
from diagrams.generic.storage import Storage
# from diagrams.aws.compute import EC2

graph_attr = {
    "fontsize": "24",
    "bgcolor": "white",
    "splines": "spline"
}
with Diagram(
             show=False, 
             direction="TB", 
             filename="knowledgeBase-application", 
             graph_attr=graph_attr
             ):
    # consumer = Person(
    #     name="Researcher", description="A user interested in AI/ML technology."
    # )
    consumer = Custom("Researcher", "logo-images/computer-user.png")
    ## llama_index is a system that generates datasets from internet searches and from knowledge in the model
    internet = Custom("internet", "logo-images/internet-icon.png")   

    with SystemBoundary("Knowledge Base Application"):
      with SystemBoundary("User Interface"):
        chatbot = Custom("chatbot\nGUI", "logo-images/chatbot.png")
        external_apis = Custom("external apis", "logo-images/api-integration-icon.png")
        context = Custom("Context", "logo-images/memory-icon.png")
        consumer >> Relationship("Specified User Question as Prompt") >> chatbot
        chatbot >> Relationship("Adds System Prompts") >> context
        chatbot >> Relationship("Invokes apis registered as tools") >> external_apis >> Relationship("adds tool messages") >> context
        chatbot >> Relationship("Returns returns results") >> consumer    

      with SystemBoundary("Fine Tuning pipeline"):
        unfiltered_dataset = Storage("Raw Dataset \n(jsonl format)")
        filtered_dataset = Storage("Filtered Dataset")
        # cc_vector_database = Custom("vector database", "logo-images/pinecone-logo.png")
        # cc_vector_database = Database("vector database")
        cc_vector_database = Custom("vector database", "logo-images/vector-database.png")
        cc_llama_index = Custom("llama_index", "logo-images/llamaindex-logo.png") 
        cc_llama_index >> Relationship('receives unstructured data') >> internet >> Relationship('searches for data') >> cc_llama_index
        cc_NemoCurator_retrievers = Custom("nemo Curator data retrievers", "logo-images/nemo-retriever.png")   
        cc_NemoCurator_retrievers >> Relationship('receives unstructured data') >> internet >> Relationship('searches for data') >> cc_NemoCurator_retrievers
        cc_NemoCurator_filters = Custom("nemo Curator filters", "logo-images/nemo-curator.png")   

      cc_NemoCurator_retrievers >> Relationship("generates") >> unfiltered_dataset
      cc_llama_index >> Relationship("generates") >> unfiltered_dataset
      cc_NemoCurator_filters >> Relationship(label="reads") >> cc_NemoCurator_filters
      cc_NemoCurator_filters >> Relationship(label="creates") >> filtered_dataset 
      cc_vector_database >> Relationship(label="receives") >> filtered_dataset 
      chatbot >> Relationship("retrieves relevant data") >> cc_vector_database >> Relationship(label="appends relavent data")  >> context
       
      with SystemBoundary("Models"):
        cc_openai = Custom("Openai gpt-4", "logo-images/openai-logo.png")
        cc_llama = Custom("llama 3.2\n from Meta", "logo-images/llama-logo.png")
      
      chatbot >> Relationship("Invokes model with context and prompts") >> cc_openai
      chatbot >> Relationship("Invokes model with context and prompts") >> cc_llama
        

    
    
  # cc_llama_index >> [cc_NemoCurator,
  #                   cc_llama] >> cc_milvus
  