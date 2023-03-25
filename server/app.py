# create a view to handle login route

class Login(resource):
    def get(self):
        pass

    # login the the user
    def post(self):
        # look up a user in the database based on the username user fills in the form
        # get the username from the form the user fills in
        user = User.query.filter(User.username == requeset.get_json()['username']).first()
        
        # verify the login credentials, and store the authenticated user's id in the session
        # set a "user_id" session variable to the user.id
        # Flask will take the value of this session obj and serializes it into a cookie
        session["user_id"] = user.id
        return jsonify(user.to_dict())

api.add_resource(Login, '/login')



# 10. refresh the page, the state in frontend got reset, so it doesn't know which user it is
# 11. but backend still knows, so need a way of getting the user data from backend into the state with the page first loads
# first, need a route to retrieve the user's data from the database using the session hash:
# then log the user in from the frontend as soon as the application loads:
class CheckSession(Resource):
    # Stay Logging in
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return jsonify(user.to_dict())
        else:
            return jsonify({'message': "401: Not Authorized"}),  401
api.add_resource(CheckSession, '/check_session')   


# 1. user navigates to a login form on React frontend
# 2. enter username, (no ps for now)
# 3. submits the form, posting to /login on Flask backend
# 4. in login view, we set a cookie on the user's browser by writing their user ID into the session hash
# 5. user logged in, session["usr_id"] will hold their user ID

# 6. to log yourself out, have to delete the cookie from your browser
# 7. create a component for the Login and save the username in the state
# 8 .session["user_id"] is stored in the backend so it can identify us with each request using the session obj,
# 9. the frontend also knows who we are bz the user data was saved in state after logging in


class Logout(Resource):
    session["user_id"] = None
    # 204 -> request succeeded, but user doesn't need to navigate away from current page
    return jsonify({"message": "204: No Content"}), 204

api.add_resource(Logout, '/logout')