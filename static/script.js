document.getElementById('healthcare-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const response = await fetch('/submit', {
      method: 'POST',
      body: formData,
    });
    
    const result = await response.json();
    console.log(result.message);
    document.getElementById('success-message').style.display = 'block';
  });
  