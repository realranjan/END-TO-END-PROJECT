import { useState } from 'react'
import Head from 'next/head'
import PredictionForm from '../components/PredictionForm'
import PredictionResult from '../components/PredictionResult'

export default function Home() {
  const [prediction, setPrediction] = useState<number | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handlePrediction = async (formData: any) => {
    setLoading(true)
    setError(null)
    
    try {
      const response = await fetch('/api/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })
      
      if (!response.ok) {
        throw new Error('Prediction failed')
      }
      
      const result = await response.json()
      setPrediction(result.predicted_math_score)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <Head>
        <title>Student Performance Predictor</title>
        <meta name="description" content="Predict student math scores using machine learning" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      
      <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
        <div className="container mx-auto px-4 py-8">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold text-gray-900 mb-4">
              Student Performance Predictor
            </h1>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Predict student math scores based on demographic and academic factors using advanced machine learning algorithms
            </p>
          </div>
          
          <div className="max-w-4xl mx-auto grid md:grid-cols-2 gap-8">
            <div className="card">
              <h2 className="text-2xl font-semibold text-gray-800 mb-6">
                Enter Student Information
              </h2>
              <PredictionForm onSubmit={handlePrediction} loading={loading} />
            </div>
            
            <div className="card">
              <h2 className="text-2xl font-semibold text-gray-800 mb-6">
                Prediction Results
              </h2>
              {loading && (
                <div className="text-center py-8">
                  <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto"></div>
                  <p className="mt-4 text-gray-600">Analyzing student data...</p>
                </div>
              )}
              
              {error && (
                <div className="bg-red-50 border border-red-200 rounded-lg p-4">
                  <p className="text-red-800">{error}</p>
                </div>
              )}
              
              {prediction !== null && !loading && (
                <PredictionResult score={prediction} />
              )}
              
              {!loading && !error && prediction === null && (
                <div className="text-center py-8 text-gray-500">
                  <p>Enter student information to get a prediction</p>
                </div>
              )}
            </div>
          </div>
        </div>
      </main>
    </>
  )
} 