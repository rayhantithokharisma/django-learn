from django.shortcuts import render

def home(request):
    name = "Rayhan Titho Kharisma"  # Replace with your name
    email = "rayhantithokharisma@gmail.com"  # Your email
    github_link = "https://github.com/rayhantithokharisma"  # Your GitHub link
    linkedin_link = "https://www.linkedin.com/in/rayhan-titho-80b5b2158/"  # Your LinkedIn link

    experiences = [
        {
            "title": "Worked at Kredivo",
            "points": [
                "During my time at Kredivo, I was responsible for developing and refining credit scoring models.",
                "Voice Modeling: My role also encompassed voice modeling, a cutting-edge technology in the financial sector. I was part of a team that leveraged voice data to enhance customer identification and security measures."
            ],
        },
        {
            "title": "Worked at Freeport",
            "points": [
                "At Freeport, I was part of a team dedicated to safety analytics. I was responsible for collecting and analyzing data related to safety incidents and near misses.",
                "Operator Analytics: In the realm of operator analytics, I worked with data to optimize the performance of heavy machinery and equipment used in mining operations. I developed models to predict maintenance needs, ensuring that equipment downtime was minimized."
            ],
        },
        # Add more experiences as needed
    ]

    return render(request, 'index.html', {'name': name, 'email': email, 'github_link': github_link, 'linkedin_link': linkedin_link, 'experiences': experiences})
