import React from 'react'

interface PredictionResultProps {
  score: number
}

export default function PredictionResult({ score }: PredictionResultProps) {
  const getScoreColor = (score: number) => {
    if (score >= 80) return 'text-green-600'
    if (score >= 60) return 'text-yellow-600'
    return 'text-red-600'
  }

  const getScoreLevel = (score: number) => {
    if (score >= 80) return 'Excellent'
    if (score >= 70) return 'Good'
    if (score >= 60) return 'Average'
    if (score >= 50) return 'Below Average'
    return 'Needs Improvement'
  }

  const getScoreIcon = (score: number) => {
    if (score >= 80) return '🎯'
    if (score >= 60) return '📊'
    return '📚'
  }

  return (
    <div className="text-center">
      <div className="mb-6">
        <div className="text-6xl mb-4">{getScoreIcon(score)}</div>
        <h3 className="text-2xl font-bold text-gray-800 mb-2">
          Predicted Math Score
        </h3>
        <div className={`text-5xl font-bold ${getScoreColor(score)} mb-2`}>
          {score.toFixed(1)}
        </div>
        <p className="text-lg text-gray-600">
          {getScoreLevel(score)}
        </p>
      </div>

      <div className="bg-gray-50 rounded-lg p-4 mb-6">
        <h4 className="font-semibold text-gray-800 mb-2">Score Interpretation</h4>
        <div className="text-sm text-gray-600 space-y-1">
          <p>• <span className="font-medium">80-100:</span> Excellent performance</p>
          <p>• <span className="font-medium">70-79:</span> Good performance</p>
          <p>• <span className="font-medium">60-69:</span> Average performance</p>
          <p>• <span className="font-medium">50-59:</span> Below average</p>
          <p>• <span className="font-medium">0-49:</span> Needs improvement</p>
        </div>
      </div>

      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <h4 className="font-semibold text-blue-800 mb-2">💡 Recommendations</h4>
        <div className="text-sm text-blue-700 space-y-1">
          {score < 60 && (
            <>
              <p>• Consider additional math tutoring</p>
              <p>• Focus on fundamental concepts</p>
              <p>• Practice with sample problems daily</p>
            </>
          )}
          {score >= 60 && score < 80 && (
            <>
              <p>• Review challenging topics</p>
              <p>• Practice advanced problems</p>
              <p>• Consider enrichment programs</p>
            </>
          )}
          {score >= 80 && (
            <>
              <p>• Maintain current study habits</p>
              <p>• Challenge yourself with advanced topics</p>
              <p>• Consider mentoring other students</p>
            </>
          )}
        </div>
      </div>
    </div>
  )
} 