import requests
import datetime

# user creds for the pixela
user_name = "pixela-username"
token = "pixela-token"
header = {
    'X-USER-TOKEN' : token
}
graph_id = 'graph-id-here-from-pixela'


# this function creates the user in pixe.la
def create_user():
    global pix_endp
    pix_endp = "https://pixe.la/v1/users"
    user_data = {
        "token": token, 
        "username": user_name, 
        "agreeTermsOfService":"yes", 
        "notMinor":"yes"
    }
    c_user = requests.post(url=pix_endp,json=user_data)
    print(c_user.text)


# this function creates the graph in your pixela account see documentation
def create_graph():
    global  graph_endp
    graph_endp = f"{pix_endp}/{user_name}/graphs"
    graph_id = graph_id
    graph_params = {
        'id': graph_id,
        'name' : 'Running Graph',
        'unit' : 'km',
        'type' : 'float',
        'color': 'ajisai',
        }

    graph_creation = requests.post(url=graph_endp,json=graph_params,headers=header)
    print(graph_creation.text)


# just formating the date to use in the programe
today = datetime.datetime.today()
fdate = today.strftime("%Y%m%d")


# loop over to continue the command line interface to intract with the code
userresponse = 9
def continue_programe():
    global userresponse
    user_response_init = int(input("1- Post Your Activity to Calender  \n2- Delete the Activity  \n3- Edit the Activity  \n0- Exit the programe  "))
    # terminating the programe
    if user_response_init == 0:
        return 0
    # adding data to pixel
    elif user_response_init == 1:
        walksinkm = input("Put your Today Walking history to Calender (km):  ")
        user_date = input("For which date you want to Delete the Activity %(YYYYMMDD):  ")
        postpixel_endp = f"https://pixe.la/v1/users/{user_name}/graphs/{graph_id}"
        postpixel_prams = {
            "date":user_date,
            "quantity":walksinkm
        }
        pixel_post = requests.post(url=postpixel_endp,json=postpixel_prams,headers=header)
        print(pixel_post.json()['message'])

    # deleting the pixel 
    elif user_response_init == 2:
        user_date = input("For which date you want to Delete the Activity %(YYYYMMDD):  ")
        pixel_dl_endp = f"https://pixe.la/v1/users/{user_name}/graphs/{graph_id}/{user_date}"
        pixel_dl_edit = requests.delete(url=pixel_dl_endp,  headers=header)
        print(pixel_dl_edit.json()['message'])
    # editing the existing data
    elif user_response_init == 3:
        user_date = input("For which date you want to Edit the Activity %(YYYYMMDD):  ")
        user_quantity = input("How many km you want to put there:  ")
        pixeledit_endp = f"https://pixe.la/v1/users/{user_name}/graphs/{graph_id}/{user_date}"
        pixeledit_params = {
            "quantity" : user_quantity
        }
        pixel_is_being_edit = requests.put(url=pixeledit_endp,  json=pixeledit_params,  headers=header)
        print(pixel_is_being_edit.json()['message'])







# this checks the data for today if empty then calls the main fucntion to intract with the code otherwise break
while userresponse != 0:
    # checking the today pixel if empty adding the data
    get_a_pixel_endp = f"https://pixe.la/v1/users/{user_name}/graphs/{graph_id}/{fdate}"
    response = requests.get(url=get_a_pixel_endp,headers=header)
    response_data = response.json()
    try:
        if response_data['quantity']:
            print(f"Your today Walking history is: {response_data['quantity']} km")
            returnd = continue_programe()
            if returnd == 0:
                break
    except:

            returnd = continue_programe()
            if returnd == 0:
                break
