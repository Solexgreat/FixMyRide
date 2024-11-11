import React from 'react';
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
// import { Swiper, SwiperSlide } from 'swiper/react';
// import 'swiper/css';
// import 'swiper/css/navigation';
// import 'swiper/css/pagination';
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
		getImageSrc: () => require("../image/slide 2.jpg"),
		a: 'Brake_Repair',
	},

	{
		id: 3,
		Name: "Battery Replacement",
		Description: "Checking and replacing car batteries to ensure reliable engine starts and electrical performance",
		getImageSrc: () => require("../image/slide 1.jpg"),
		a: 'Battery Replacement'
	},

	{
		id: 4,
		Name: "Tire Rotation and Replacement",
		Description: "Rotating tires to prevent uneven wear, and replacing tires when tread is worn down.",
		getImageSrc: () => require("../image/slide 3.jpg"),
		a: 'Battery Replacement'
	}
]

const NextArrow = ({ onClick }) => (
    <div
        className="slick-arrow slick-next"
        onClick={onClick}
        style={{
            fontSize: '2rem', 
            color: '#ff5733', // Change color here
            right: '10px', 
            zIndex: 1
        }}
    >
        &#10095;
    </div>
);

const PrevArrow = ({ onClick }) => (
    <div
        className="slick-arrow slick-prev"
        onClick={onClick}
        style={{
            fontSize: '2rem',
            color: '#ff5733', // Change color here
            left: '10px',
            zIndex: 1
        }}
    >
        &#10094;
    </div>
);


function ServiceSection() {

	var settings = {
    infinite: true,
    speed: 500,
    slidesToShow: 3,
    slidesToScroll: 1,
		nextArrow: <NextArrow />,
    prevArrow: <PrevArrow />
  };
	return (
		<section className="popular-service">
		<h2>Popular Services</h2>
		 {/* <Swiper
			spaceBetween={20}
			slidesPerView={3}
			loop={true}
			navigation
			pagination={{ clickable: true }}
			autoplay={{ delay: 3000 }}
			breakpoints={{
				768: {
					slidesPerView: 2,
				},
				1024: {
					slidesPerView: 3,
				},
			}}
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
			))} */}
		{/* </Swiper> */}
		<div className='slider'>
			<Slider {...settings}>
				{popularServices.map((service) => (
					<a href={`#${ service.a}`}>
						<div className='Card'>
							<div className='image'>
								<img src= {service.getImageSrc()} alt="" / >
							</div>
							<div className='card-text'>
								<h3>{service.Name}</h3>
								<p>{service.Description}</p>
							</div>
						</div>
					</a>
				))}
			</Slider>
		</div>
	</section>
	)
}

export default ServiceSection