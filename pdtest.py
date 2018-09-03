import programdirector
pd = programdirector.ProgramDirector({
    "courses":[
        {"id":"MIS605"},
        {"id":"MBA576"},
        {"id":"MIS603",
         "prereqs":["MIS605"]
         },
        {"id":"MIS607",
         "prereqs":["MIS605"]
         },
        {"id":"MIS609",
         "prereqs":["MIS605"]
         },
        {"id":"CIS604",
         "prereqs":["MIS605"]
         },
        {"id":"MIS614",
         "prereqs":["MIS605"]
         },
        {"id":"CIS606",
         "prereqs":["MIS614"]
         },
        {"id":"CIS607",
         "prereqs":["MIS614"]
         },
        {"id":"CIS608",
         "prereqs":["MIS614"]
         },
        {"id":"CIS609",
         "prereqs":["MIS614"]
         },
        {"id":"CIS610",
         "prereqs":["MIS605","MIS603","MIS607","MIS609","CIS604","MBA576","CIS606","CIS607","CIS608","CIS609"]
         },        
        ],
    "terms":[{"id":"S1"},{"id":"S2"},{"id":"U"},{"id":"F1"},{"id":"F2"}]
    })

pd.info()
test = pd.test_schedule("S2",{
    "S1":["MIS605","MIS603","MIS614","MBA576","CIS606","CIS607","CIS610"],
    "S2":["MIS603","MIS605","MIS609","MBA576","CIS604","CIS609","CIS610"],
    "U":["MIS614","MBA576", "CIS604"],
    "F1":["MIS605","MIS607","MIS614","MBA576","CIS606","CIS610"],
    "F2":["MIS603","MIS605","MIS609","MIS614","MBA576","CIS604","CIS608","CIS609","CIS610"]
    }, 1, 12)
print (test)
print (pd.longest)
