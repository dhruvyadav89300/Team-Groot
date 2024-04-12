import ollama

system_prompt = """
You are a teacher. You have a 10+ years of experience in teaching. Your students love you because you make them understand complex topics in easy words.
Now Student will give an article about any study related topic below after the colon sign. You have to summarize it in such a way that you convey all the 
essential meaning of the article in very few words. Make sure you do not skip key words. You are not allowed to return anything else other the summary.
Student's Article: 
"""

def summarizer(system_prompt, user_query):
    final_prompt = system_prompt + user_query
    response = ollama.generate(
        model="llama2",
        prompt=final_prompt
    )
    return response["response"]

a = """
Newton’s First Law of Motion, also known as the Law of Inertia, is a fundamental principle that describes the behaviour of objects in the absence of external influences. The term “Law of Inertia” emphasizes the concept of inertia, which refers to the property of massive objects to resist changes in their state of motion. This idea stems from the observation that objects naturally maintain their current state of rest or motion, resisting any changes unless acted upon by an external force.
By naming the first law of motion the “Law of Inertia,” Newton highlighted this inherent property of objects and laid the groundwork for understanding how forces can cause changes in motion. Newton’s first law of motion states that objects persist in their current state of motion unless compelled to do otherwise by an external force. Whether an object is at rest or in uniform motion, it will continue in that state unless a net external force acts upon it.
One crucial insight provided by Newton’s First Law is that the object will maintain a constant velocity in the absence of a net force resulting from unbalanced forces acting on an object. If the object is already in motion, it will continue moving at the same speed and direction. Likewise, if the object is at rest, it will remain stationary. However, introducing an additional external force will cause the object’s velocity to change, responding to the magnitude and direction of the force applied.
Understanding Newton’s First Law of Motion sets the stage for a deeper exploration of the subsequent laws that govern the complexities of motion. By comprehending this fundamental principle, we gain crucial insights into how objects behave independently and how external forces influence their motion. The first law of motion provides a strong foundation for further understanding the dynamics and behaviour of objects in the physical world.
"""
print(summarizer(system_prompt, a))