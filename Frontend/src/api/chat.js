const getResponse = async (userMessage)=>{
    try {
        console.log(userMessage);
        const response = await fetch('http://localhost:8000/chat-completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ query: String(userMessage) }),
        });
  
        if (!response.ok) {
          throw new Error('Failed to fetch bot response');
        }
        const data = await response.json();
        const botMessage = data;
        return botMessage;
        
      } catch (error) {
        console.error('Error:', error);
      }
    }

export default getResponse;    
