import pandas as pd
from sklearn.model_selection import train_test_split

namelist = pd.DataFrame({
        "name" : ["Suzuki","Tanaka","Yamada","Watanabe","Yamamoto","Okada","Ueda","Inoue","Hayashi","Sato",
                "Hirayama","Shimada"],
        "aga":[30,40,55,29,41,28,42,24,33,39,49,53],
        "department":["HR","Legal","IT","HR","HR","IT","Legal","Legal","IT","HR","Legal","Legal"],
        "attendance":[1,1,1,0,1,1,1,0,0,1,1,1]
})

print(namelist)

namelist_train,namelist_test = train_test_split(namelist,test_size=0.3)
print("-------------------------train dataset-------------------------\n",namelist_train)
print("-------------------------test dataset--------------------------\n",namelist_test)