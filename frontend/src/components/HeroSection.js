import React from 'react'
// import ReactDOM from 'react-dom';
import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css"; 


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
		text: 'Your vehicle is in good hands with our teamof skilled professionals',
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
		<section>
			{/* Mobile phone */}
			<div className="heroSection phones">
				<Carousel>
					<img src={ require("../image/slide 1.jpg")} alt="Hero_image" />
					<h1>Book an Appointment in Minutes </h1>
					<h1> in Minutes!</h1>
					<p>Easily schedule appointments with
						trusted mechanics at your convenience
					</p>
					<button>
						Book an Appointment
					</button>
				</Carousel>
			</div>
			{/* Lager screen */}
			<div className='carousel'>
				<Carousel className='carousell'  showThumbs={false}  autoPlay infiniteLoop>
					{slides.map((slide, index) =>
					<div className='carousel heroSection'>
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
			</div>
		</section>
	)
}


export default HeroSection