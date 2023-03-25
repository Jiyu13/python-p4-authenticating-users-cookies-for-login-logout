// log the user in from the frontend as soon as the application loads
function App() {

    const [user, setUser] = useState(null)

    useEffect(() => {
        fetch('/check_session')
        .then((r) => {
            if (r.ok) {
                r.json().then((user) => setUser(user))
            }
        })
    }, []);

    if (user) {
        return <h2>Welcome {user.username}</h2>
    } else {
        return <Login onLogin={setUser} />
    }
}

export default App