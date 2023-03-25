function Navbar( {onLogout}) {
    function handleLogout() {
        fetch('/logout', {
            method: 'DELETE'
        }).then(() => onLogout())   // onLogout() would handle removing the infor about the user from state
    }

    return (
        <header>
            <button onClick={handleLogout}>Logout</button>
        </header>
    )
}