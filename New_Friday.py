import pprint
import google.generativeai as palm

palm.configure(api_key="AIzaSyCmumtK86Acdh7dSCsbeMSs9CNxf2djDvw")


models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)