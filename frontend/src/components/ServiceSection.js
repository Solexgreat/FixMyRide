import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
// import 'swiper/swiper-bundle.min.css';


const popularServices = [
	{
		id: 1,
		Name: "Oil Change",
		Description: "Replacing the old engine oil and oil filter to ensure the engine runs smoothly and efficiently",
		getImageSrc: () => require("../image/slide 3.jpg")
	},

	{
		id: 2,
		Name: "Brake Repair and Replacement",
		Description: "Inspection, repair, and replacement of brake pads, rotors, and calipers to maintain safe braking.",
		getImageSrc: () => require("../image/slide 2.jpg")
	},

	{
		id: 3,
		Name: "Battery Replacement",
		Description: "Checking and replacing car batteries to ensure reliable engine starts and electrical performance",
		getImageSrc: () => require("../image/slide 1.jpg")
	},

	{
		Name: "Tire Rotation and Replacement",
		Description: "Rotating tires to prevent uneven wear, and replacing tires when tread is worn down.",
		getImageSrc: () => require("../image/slide 3.jpg")
	}
]


function ServiceSection() {
	return (
		<section className="popular-service">
		<h2>Popular Services</h2>
		<Swiper
			spaceBetween={20}
			slidesPerView={3.2} // Adjust for partial fourth card view
			loop
			autoplay={{ delay: 3000 }}
			className="popular-service-carousel"
		>
			{popularServices.map(service => (
				<SwiperSlide key={service.id}>
					<div className="service-card" style={{ width: 454, height: 552 }}>
						<img src={service.getImageSrc()} alt={service.title} className="service-image" />
						<h3>{service.Name}</h3>
						<p>{service.Description}</p>
					</div>
				</SwiperSlide>
			))}
		</Swiper>
	</section>
	)
}

export default ServiceSection