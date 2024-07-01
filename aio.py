import requests
import urllib.parse
from multiprocessing.pool import ThreadPool
import time

# Dictionary containing canvas_session tokens for different members
canvas_sessions = {
    # e.g. "elmo": "N539PIHvxk3tOJJOQYa6zA+NMw_Lcs8V3Pgb-OeEMiJLUVDjolf262bpdGufBjtlSh5NEILQO0D_wmpfv_1PsGt61raYMC7g46T2T4w-5h2zxNKy_F9VmBjH6OUhXDGtYNulTRuYo7WvcLtMUmTbmHSqAqNRvzn_3GV46DxE1uNaywpUseX7i_X8r5V48sN8tMUfdsYpLbWBWQK7FZZ6BN84r7DIMVL8iGJbtCmRrLAYAtpJMvjZMqPvg5V1nhhx9Y9V60mdmC51NhrUUSej9e9waHhb5j6LH7aLQ0C1cKLEBNToqcvB8CN8RpFJ5R_OpN7bQSPSLyU56owgWsVoi6uFBBeKAHYmE1p1hSeG7MWVYo_JQf4SQPMOIBmJBybNsT_NxEx5G7BXhyQLofyUzKJWQwg4yETH6llhv-dTdzTOHOATl0NMGYR5z3uNcICKGABSZF5ItGS-As93accmYtDsBjGaMq33yezH-tRJHIhV-TdORK83ikIqEmG6iwPfJoOldojvfzrFFqPjQdPBkuF5rxe2aVwvpk-HTzA6Bg2QoHD022ekd0D6-oRDiBXeFfGM4z4OxU26AQHxLddBn7U4LJDMKRXrSO74pWTitvOe4P8HfzHwl3L8n6p5xeVJq-6CRM-sF6w6EFwBRlZqQ9HW4OM-BQo803caLASfPIOhTHu4cm2vs3LjrYcjTofvFk2m8xmhlF6wTZIOvr12vNS.S2-kkaQfFGvKpyxr3gx3D3nbOhM.Zdwo8w",
    "member1": "canvas_session",
    "member2": "canvas_session",
    "member3": "canvas_session",
    "member4": "canvas_session",
    "member5": "canvas_session",
    "member6": "canvas_session",
}

# Encoded _csrf_token for form submission
# e.g. uWe55qNzL4f9%2FeHE1miASbvjSR%2BKSt1aBBX7oTMCk%2BrcXtKjjD5OtbybiKnvUPIN0atibPly7Qx1Y8rFY3PwuA%3D%3D
en_csrf_token = "_csrf_token"
# Decoded _csrf_)token used as authenticty_token
de_csrf_token = urllib.parse.unquote(en_csrf_token)

# Monitor delay in seconds, decrease delay closer to the time
delay = 30
# Group ID
group_id = "143065"

def join_group(canvas_session):
    '''Function to join a group using the provided canvas_session token.'''
    # Define cookies with the canvas_session token and CSRF token
    cookies = {
        'canvas_session': canvas_session,
        '_csrf_token': en_csrf_token,
    }

    # Define data for the POST request to join the group
    data = {
        'user_id': 'self',
        '_method': 'POST',
        'authenticity_token': de_csrf_token,
    }

    # Send POST request to join the group
    response = requests.post(
        url=f"https://swinburne.instructure.com/api/v1/groups/{group_id}/memberships",
        cookies=cookies,
        data=data,
    )

    return response.status_code, response.content

def leave_group(canvas_session):
    '''Function to leave a group using the provided canvas_session token.'''
    # Define cookies with the canvas_session token and  _csrf_token
    cookies = {
        'canvas_session': canvas_session,
        '_csrf_token': en_csrf_token,
    }

    # Define data for the POST request to leave the group
    data = {
        '_method': 'DELETE',
        'authenticity_token': de_csrf_token,
    }

    # Send POST request to leave the group
    response = requests.post(
        url=f'https://swinburne.instructure.com/api/v1/groups/{group_id}/memberships/self',
        cookies=cookies,
        data=data,
    )

    return response.status_code, response.content

if __name__ == '__main__':

    # Create a thread pool with n threads
    pool = ThreadPool(processes=len(canvas_sessions))
    
    print(f"Starting Monitor. delay={delay}s")

    while True:
        # Define cookies with the canvas_session token
        cookies = {
            'canvas_session': list(canvas_sessions.values())[0],
        }

        # Define parameters with the include[], page number, and per_page quantity
        # Limit per_page to 1 for more efficient monitoring
        params = {
            'include[]': 'permissions',
            'page': 'XXX',
            'per_page': '1',
        }
        
        # Send GET request to API to retrieve group permissions
        response = requests.get(
            'https://swinburne.instructure.com/api/v1/courses/____/groups',
            params=params,
            cookies=cookies,
        )

        # Convert response to JSON and access permissions of the first group
        response_json = response.json()[0]["permissions"]

        # Check if joining groups is permitted
        if response_json["join"]:
            time_start = time.time() # Start time
            print("join:true. Starting Bot")
            # Use pool to execute join_group/leave_group for each canvas_session token
            results = pool.map(join_group, canvas_sessions.values())
            # Print results of join_group executions
            for result in results:
                print(result)
        else:
            # If joining groups is not permitted, wait for a specified delay
            print(f"join:false. Sleeping {delay}s...")
            time.sleep(delay)