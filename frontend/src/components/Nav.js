import React, {useState} from 'react'

function Nav() {
	const[menuOpen, setMenuOpen] = useState(false);


	const toggleMenu = () => {
		setMenuOpen(!menuOpen);
	}
	return (
		<nav className='nav-bar'>
			<a href='/' className="logo">
				<h1>FixMyRide</h1>
			</a>
			<div className="nav-desktop">
				{/* <a href='/' className="logo"> */}
					{/* <h1>FixMyRide</h1> */}
				{/* </a> */}

				<ul>
					<li><a href='#Home'>HOME</a></li>
					<li><a href='#About'>ABOUT</a></li>
					<li><a href='#Service'>SERVICES</a></li>
					<li><a href='#Contact Us'>CONTACT</a></li>
				</ul>

				<div className="registration-btn">
					<button>Sign in</button>
					<button>Sign up</button>
				</div>
			</div>

			{/*mobile menu*/}
			<div className="menu-bar" onClick={toggleMenu}>
				<div className="menu-bar bar"></div>
				<div className="menu-bar bar"></div>
				<div className="menu-bar bar"></div>
				<div className="menu-bar bar"></div>
			</div>

			<ul className={`nav-links ${menuOpen ? "visible": " "}`}>
				<li><a href='#Home'>HOME</a></li>
				<li><a href='#About'>ABOUT</a></li>
				<li><a href='#Service'>SERVICES</a></li>
				<li><a href='#Contact Us'>CONTACT</a></li>
				<li><a href='#Sing in'>Sing in</a></li>
				<li><a href='#Sing us'>Sing us</a></li>
			</ul>
		</nav>
	)
}

export default Nav