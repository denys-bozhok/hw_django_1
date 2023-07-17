from django.shortcuts import render
from django.http import HttpResponse


todo_list = [
    {
        "id": 1,
        "title": "Walk with Sobaken",
        "discription": "Walk with dog near 30 min, where it make a crap twice"
    },
    
    {
        "id": 2,
        "title": "Go to gun-shop",
        "discription": "Buy a huge revolver and a box of cartridges for it"
    },
    
    {
        "id": 3,
        "title": "Walk with Sobaken",
        "discription": "Walk with dog near 30 min, where it make a crap twice"
    },
    {
        "id": 4,
        "title": "Rob the police station",
        "discription": "Unobtrusively launch the dog into the room with material evidence, give the radio command 'Steal cocaine and heads', wait until the dog digs a tunnel for itself, put it behind the wheel and leave the territory."
    },
    
    {
        "id": 5,
        "title": "Get Sobaken into a rock band",
        "discription": "With the help of cocaine, meet a rock band and record a joint song with a dog"
    },
    
    {
        "id": 6,
        "title": "Pick up a girl",
        "discription": "Pretend to be a dog agent and snatch the girl"
    },
    
    {
        "id": 7,
        "title": "Shoot a box of ammo",
        "discription": "During carnal pleasures, put a cowboy hat on a girl, make her jump on top and shoot a revolver 3 times, each time she cums. Shoot the whole box of ammo."
    },
    
    {
        "id": 8,
        "title": "Have breakfast",
        "discription": "Have breakfast with berries and cream licked from the girl's boobs and vagina"
    },
    
    {
        "id": 9,
        "title": "Learn python",
        "discription": "turn in your Python homework to your favorite teacher and tell him in this Easter egg that he is just Nyashka"
    },
]

# Create your views here.

def get_todo_list(req):
    string = ""
    for deal in todo_list:
        string += f"""
        <div>
            <h4>{deal['id']}</h4>
            <a href='{deal["id"]}'>{deal['title']}</a>
        </div>
        """
    return HttpResponse(string)
    

def get_deal(req, id):
    string = ""
    leth_todo_list = len(todo_list)
    
    for deal in todo_list:
        if deal['id'] == id:
            string += (f"""
            <div>
                <h2>{deal['id']}</h2>
                <h4>{deal['title']}</h4>
                <br>
                <p>{deal['discription']}</p>
                <br>
            """)
            if id == 1:
                string += (f"""
                    <a href="{deal["id"] + 1}">NEXT-></a>
                </div>
                """)
            elif id == leth_todo_list:
                string += (f"""
                    <a href="{deal["id"] - 1}"><-PREV</a>
                </div>
                """)
            else:
                string += (f"""
                    <a href="{deal["id"] - 1}"><-PREV</a>
                    <a href="{deal["id"] + 1}">NEXT-></a>
                </div>
                """)
                
    return HttpResponse(string)