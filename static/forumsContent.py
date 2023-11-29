def whichForum(key):
    forumList = forums[key]
    forum = {
        'title':forumList[0],
        'context':forumList[1],
        'welcomeNote':forumList[2],
        'topic1':forumList[3],
        'topic2':forumList[4],
        'bio':forumList[5],
        'form':forumList[6],
        'imageLink':'../static/img/Logos/'+forumList[7]
        }
    return forum

def getKeys():

    return list(forums.keys())

forums = {
    'GA':
        [
        'General Assembly',


        """What is Lorem Ipsum?
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        <br>
        <br>
        Why do we use it?
        It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
        <br>
        <br>
        Where does it come from?
        Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
        <br>

        The standard chunk of Lorem Ipsum ued since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are 
        also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.""",


        """What is Lorem Ipsum?
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        <br>
        <br>
        Why do we use it?
        It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
        <br>
        <br>
        Where does it come from?
        Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
        <br>

        The standard chunk of Lorem Ipsum ued since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 fr
        om "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.""",


        'www.facebook.com',
        'www.instagram.com',
        'www.x.com',
        'www.google.com',
        'FGA.png',
        ],


    'AL':
        [
        'Arab League',
        """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        <br>
        <br>
        Why do we use it?
        It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
        <br>
        <br>
        Where does it come from?
        Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
        <br>

        The standard chunk of Lorem Ipsum ued since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum 
        et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.""",



        """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        <br>
        <br>
        Why do we use it?
        It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
        <br>
        <br>
        Where does it come from?
        Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
        <br>

        The standard chunk of Lorem Ipsum ued since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum 
        et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.""",
        'www.facebook.com',
        'www.instagram.com',
        'www.x.com',
        'www.google.com',
        'AL.png',
        ],


        'ECOSOC':
        [
        'United Nations Economical And Social Council',


        """
        """,


        """
        """,


        'www.facebook.com',
        'www.instagram.com',
        'www.x.com',
        'www.google.com',
        'ECOSOC.png',
        ],


        'ICJ':
        [
        'International Court Of Justice',


        """
        """,


        """
        """,


        'www.facebook.com',
        'www.instagram.com',
        'www.x.com',
        'www.google.com',
        'ICJ.png',
        ],


        'NATO':
        [
        'North Atlantic Treaty Organisation',


        """
        """,


        """
        """,


        'www.facebook.com',
        'www.instagram.com',
        'www.x.com',
        'www.google.com',
        'NATO.png',
        ],



        'UNEP':
        [
        'United Nations Environmental Programme',


        """
        """,


        """
        """,


        'www.facebook.com',
        'www.instagram.com',
        'www.x.com',
        'www.google.com',
        'UNEP.png',
        ],



        'UNHRC':
        [
        'United Nations Human Rights Council',


        """
        """,


        """
        """,


        'www.facebook.com',
        'www.instagram.com',
        'www.x.com',
        'www.google.com',
        'UNHRC.png',
        ],





        'UNRWA':
        [
        'United Nations Relief and Works Agency',


        """
        """,


        """
        """,


        'www.facebook.com',
        'www.instagram.com',
        'www.x.com',
        'www.google.com',
        'UNRWA.png',
        ],

        'UNSC':
        [
        'United Nations Security Council',


        """
        """,


        """
        """,


        'www.facebook.com',
        'www.instagram.com',
        'www.x.com',
        'www.google.com',
        'UNSC.png',
        ],

        'WHO':
        [
        'World Health Organisation',


        """
        """,


        """
        """,


        'www.facebook.com',
        'www.instagram.com',
        'www.x.com',
        'www.google.com',
        'WHO.png',
        ],






        
}


executives = [
[{'Head of Logistics':'Mutaz Rweished'},
{'Head of Logistics Assistants': 'Rahaf Hijazi, Yara Izheman',},
{'twitter':'www.twitter.com'},
{'facebook':'www.facebook.com'},
{'instagram':'www.instagram.com'},],

[{'Head of Crisis':'Tia Allawi'},
{'Head of Crisis Assistants': 'Majd Shiber',},
{'twitter':'www.twitter.com'},
{'facebook':'www.facebook.com'},
{'instagram':'www.instagram.com'},],

[{'Head of Information':' Maria Handal'},
{'Head of Information Assistants': 'Sameer',},
{'twitter':'www.twitter.com'},
{'facebook':'www.facebook.com'},
{'instagram':'www.instagram.com'},],


[{'Head of Design':'Joe Shammas'},
{'Head of Design Assistants': 'Shahd Hammoudeh, Nerine Nimri',},
{'twitter':'www.twitter.com'},
{'facebook':'www.facebook.com'},
{'instagram':'www.instagram.com'},],

[{'Head of Entertainment':'Farid Qawasmi'},
{'Head of Entertainment Assistants': 'Nada Nureldin, Zeina Shurafa, Zeena Jabr',},
{'twitter':'www.twitter.com'},
{'facebook':'www.facebook.com'},
{'instagram':'www.instagram.com'},],

[{'Heads of Food':'Fahed and Omar Harhash'},
{'Heads of Assistants':' ',},
{'twitter':'www.twitter.com'},
{'facebook':'www.facebook.com'},
{'instagram':'www.instagram.com'},],

[{'Head of Student Officers': 'Zeina Nazzal'},
{'Head of Student Officers Assistants': 'Ahmad Abu Assab',},
{'twitter':'www.twitter.com'},
{'facebook':'www.facebook.com'},
{'instagram':'www.instagram.com'},],


[{'Head of Staff':'Fuoad and Mhamoud'},
{'Head of Staff Assistants': 'Rashid Ghneim',},
{'twitter':'www.twitter.com'},
{'facebook':'www.facebook.com'},
{'instagram':'www.instagram.com'},],


[{'Head of Press and Media': 'Natalie and Nadine '},
{'Head of Pressand and Media Assistants': 'Joelle Saeed, Ashraf Awar',},
{'twitter':'www.twitter.com'},
{'facebook':'www.facebook.com'},
{'instagram':'www.instagram.com'},],

[{'Head of IT':' William Tabban'},
{'Head of IT Assistants': 'George Nassar, Ashraf Awar',},
{'twitter':'www.twitter.com'},
{'facebook':'www.facebook.com'},
{'instagram':'www.instagram.com'},],
]



ourTeam= [
    {
    'name':'Issa Odeh',
    'role':'Deputy General',
    'twitter':'www.twitter.com',
    'facebook':'www.facebook.com',
    'instagram':'www.instagram.com',
    'pfp':'team-1.jpg',
     },
     {
    'name':'Antony Saleh',
    'role':'Deputy Secretary General',
    'twitter':'www.twitter.com',
    'facebook':'www.facebook.com',
    'instagram':'www.instagram.com',
    'pfp':'team-1.jpg',
     },
     {
    'name':'Mohammad Owais',
    'role':'Director General',
    'twitter':'www.twitter.com',
    'facebook':'https://www.facebook.com/moudy.owais/',
    'instagram':'https://www.instagram.com/moudy.owais/',
    'pfp':'MO.png',
     },
     {
    'name':'Bashar Sinokrot',
    'role':'Deputy Director General',
    'twitter':'www.twitter.com',
    'facebook':'www.facebook.com',
    'instagram':'www.instagram.com',
    'pfp':'team-1.jpg',
     },
     {
    'name':'Lourd Abu Hadid',
    'role':'Under Secretary General Of Finance',
    'twitter':'www.twitter.com',
    'facebook':'www.facebook.com',
    'instagram':'www.instagram.com',
    'pfp':'team-1.jpg',
     },
     {
    'name':'Lilas Harhash',
    'role':'Under Secretary General Of Public Affairs',
    'twitter':'www.twitter.com',
    'facebook':'www.facebook.com',
    'instagram':'www.instagram.com',
    'pfp':'team-1.jpg',
     },
]

questionList = [
{'question':'Are there any MUN-related publications or resources available?','answer':'LASMUN is affliated with  "Best Delegate" organisation regarding procedure, more info is provided on the LASMUN procedure and debate flow guide as well as the delegate guide.'},

{'question':'How are awards and recognition determined in LASMUN? And how many are there?','answer':'In LASMUN a certain criteria is followed by the Student Officers, In each committee there is 1 best delegate, 3-5 Honourable Mentions (depending on committee size) and 5-7 shoutouts (depending on committee size), the only way to win and achieve your dream is through dedication, determination, hard work, and relevancy.'},

{'question':'How can I prepare for an MUN conference?','answer':'For each committee a study guide is provided by the president of the committee, filled with key information and other sources to set up your position paper.'},

{'question':'Is previous MUN experience required for LASMUN conference?','answer':'Delegates are not required to have any previous information, it is open for everyone to explore the world of MUN. However student officers are required to have past MUN experience.'},

{'question':'How long is the LASMUN conference?','answer':'LASMUN will be 4 days, more information can be found on the schedule tab'},

{'question':'Are there any age restrictions for LASMUN participants?','answer':'Delegates must be High school students, that is from 9th grade to 12th, student officers must be in 10th-12th grade'},

{'question':'What is the policy on accommodation and travel arrangements for LASMUN conference?','answer':'LASMUN can provide schools with multiple accommodation suggestion which will be arranged with the MUN director, how ever LASMUN does not cover any payments. Transportation only between the venues and the hotels will be covered through the fees transportation, other transportation fees such as bus rides from your school to the venues and back is not covered by the conference, neither any time after or before the conference'},
]


COC = [
{'title':'Respect and Decorum:','COC':'''Delegates are expected to treat all conference participants, including fellow delegates, chairs, and conference staff, with courtesy and respect.Maintain a professional and diplomatic tone in all interactions.Avoid disrespectful language, personal attacks, or offensive behavior.
'''
},
{'title':'Punctuality:','COC':'''Delegates should arrive on time for committee sessions, speeches, and scheduled conference events.Lateness may result in penalties or a loss of speaking time.
'''
},
{'title':'Dress Code:','COC':'''Delegates should adhere to the specified dress code, requiring professional or business attire.Proper attire helps maintain the seriousness and professionalism of the conference.
'''
},
{'title':'Speech and Debate Rules:','COC':'''Follow established procedures for making speeches, including adhering to time limits.Respect the speaking order and chair's guidance during debates. Properly address other delegates and maintain decorum during speeches and debates.
'''
},
{'title':'Resolution and Amendment Procedures:','COC':'''Submit written resolutions and amendments according to the provided guidelines.Follow the prescribed procedures for debating and voting on resolutions and amendments.
'''
},
{'title':'No Plagiarism:','COC':'''Do not use plagiarized or copyrighted material in speeches, position papers, or other documents.Provide proper citations when referencing external sources.
'''
},
{'title':'No Harassment or Discrimination:','COC':'''Respect the diverse backgrounds, identities, and beliefs of fellow delegates.Harassment, discrimination, or bullying of any form is strictly prohibited.
'''
},
{'title':'Cell Phone and Technology Usage:','COC':'''Turn off or silence cell phones and electronic devices during committee sessions to minimize disruptions.Use technology only for conference-related purposes when permitted.
'''
},
{'title':'Use of Official Languages:','COC':'''Usage of the English language during committee sessions.'''
},
{'title':'Code of Ethics:','COC':'''Adhere to a code of ethics that promotes honesty, integrity, transparency, and diplomacy.Uphold high moral standards in all interactions and negotiations.
'''
},
{'title':'Consequences for Violations:','COC':'''Understand that violations of the code of conduct may result in consequences such as warnings, sanctions, or expulsion from the conference.Comply with the decisions of conference chairs and organizers regarding rule violations.
'''
}
]