from dfs_app.models import Dfs_model_new



def insertRec(rec):
    # print('in')
    name,roll,img,city,contact=rec[0],rec[1],rec[2],rec[3],rec[4]
    row_data = Dfs_model_new(name=name,roll_no=roll,image=img,city=city,contact=contact)
    row_data.save()
    print('done')