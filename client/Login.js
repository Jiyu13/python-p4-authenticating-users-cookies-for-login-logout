function Login( {onLogin} ) {
    const [username, setUsername] = useState("");

    function handleSubmit(e) {
        e.preventDefault(e)

        fetch("/login", {
            method: "POST",
            headers: {"Content_Type": "application/json"},
            body: JSON.stringify({username})
        })
        .then((r) => r.json())
        .then((user) => onLogin(user))
    }


    return (
        <form onSubmit={handleSubmit}>
            <input 
                type="text"
                value={usrname}
                onChange={(e) => setUsername(e.target.value)}
            />
            <button type="submit">Login</button>
        </form>
    )

}

export default Login;

// once the form is submitted, user is logged in
// the onLogin callback func handle saving the logged in user's details in state