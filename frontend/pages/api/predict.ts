import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' })
  }

  try {
    // Use the actual backend URL directly
    const backendUrl = 'https://student-predictor-backend.onrender.com'
    
    console.log('Sending request to backend:', `${backendUrl}/api/predict`)
    console.log('Request body:', req.body)
    
    const response = await fetch(`${backendUrl}/api/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(req.body),
    })

    console.log('Backend response status:', response.status)

    if (!response.ok) {
      const errorText = await response.text()
      console.error('Backend error response:', errorText)
      throw new Error(`Backend error: ${response.status} - ${errorText}`)
    }

    const data = await response.json()
    console.log('Backend response data:', data)
    res.status(200).json(data)
  } catch (error) {
    console.error('API Error:', error)
    res.status(500).json({ 
      message: 'Internal server error',
      error: error instanceof Error ? error.message : 'Unknown error'
    })
  }
} 