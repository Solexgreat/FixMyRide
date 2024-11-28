import React from 'react'
// import ReactDOM from 'react-dom';
import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css"; 
import { Link } from 'react-router-dom';


const slides = [
	{
		id: 1,
		getImageSrc: () => require("../image/slide 1.jpg"),
		header: 'Book Your Car Repair in Minutes!',
		text: 'Easily schedule appointments with trusted mechanics at your convenience',
		btn: 'Book an Appointment'
	},

	{
		id: 2,
		getImageSrc: () => require("../image/slide 2.jpg"),
		header: 'Professional Service from Ceritified Mechanics',
		text: 'Your vehicle is in good hands with our team of skilled professionals',
		btn: 'Meet Our Team'
	},

	{
		id: 3,
		getImageSrc: () => require("../image/slide 3.jpg"),
		header: 'No Surprises-Trasparent Pricing',
		text: 'View pricing upfront and manage payments effortlessly through the app',
		btn: 'View Service & Pricing'
	}
]


function HeroSection() {

	return (
		<header>
			<section className='HeroSection'>
				{/* Mobile phone */}
				{/* <div className="heroSection phones">
					<Carousel className='mobile-carousel' width="100%" showThumbs={false}  autoPlay infiniteLoop>
						{slides.map((slide, index) =>
							<div className='phone-carousel slide'>
								<img src={slide.getImageSrc()} alt="Hero_image" />
								<div className='Hero-text'>
									<h1>{slide.header}</h1>
									<p>{slide.text}</p>
									<button>
										Book an Appointment
									</button>
								</div>
							</div>
							)}
					</Carousel>
				</div> */}
				{/* Lager screen */}
				<div className='heroSection-carousel'>
					<div className='smallScreen'>
						<img src= {require("../image/slide 1.jpg")} alt='Hero-image' />
						<div className='Hero-text'>
								<h1>Book Your Car Repair in Minutes!</h1>
								<p>Easily schedule appointments with trusted mechanics at your convenience</p>
								<button>
									Book an Appointment
								</button>
							</div>
					</div>
				</div>
				<Carousel className='carousel-inner'  showThumbs={false} width='100%'  autoPlay infiniteLoop showIndicators={false}>
					{slides.map((slide, index) =>
					<div className='carousel-slide'>
						<img src={slide.getImageSrc()} alt="Hero_image" style={{height: '600px', }}  />
						<div className='Hero-text'>
							<h1>{slide.header}</h1>
							<p>{slide.text}</p>
							<Link to='/appointments'><button aria-label='On Click'>
								{slide.btn}
							</button></Link>
						</div>
					</div>
					)}
				</Carousel>
			</section>
		</header>
	)
}


export default HeroSection