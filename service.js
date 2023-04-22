const createService = async (name, price, category) => {
    const data = {
      name: name,
      price: price,
      category: category
    };
  
    const response = await fetch('/service', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
  
    if (!response.ok) {
      const errorMessage = await response.text();
      throw new Error(errorMessage);
    }
  
    const responseData = await response.json();
    return responseData;
  };

  try {
    const newService = await createService('Service Name', 100, 'Category');
    console.log('Service created:', newService);
  } catch (error) {
    console.error('Error creating service:', error);
  }