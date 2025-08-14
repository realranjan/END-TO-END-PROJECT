import { useState } from 'react'

interface PredictionFormProps {
  onSubmit: (data: any) => void
  loading: boolean
}

export default function PredictionForm({ onSubmit, loading }: PredictionFormProps) {
  const [formData, setFormData] = useState({
    gender: '',
    race_ethnicity: '',
    parental_level_of_education: '',
    lunch: '',
    test_preparation_course: '',
    reading_score: '',
    writing_score: ''
  })

  const handleChange = (e: React.ChangeEvent<HTMLSelectElement | HTMLInputElement>) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    
    // Validate form
    const hasEmptyFields = Object.values(formData).some(value => !value)
    if (hasEmptyFields) {
      alert('Please fill in all fields')
      return
    }
    
    // Convert scores to numbers
    const submissionData = {
      ...formData,
      reading_score: parseFloat(formData.reading_score),
      writing_score: parseFloat(formData.writing_score)
    }
    
    onSubmit(submissionData)
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Gender *
        </label>
        <select
          name="gender"
          value={formData.gender}
          onChange={handleChange}
          className="input-field"
          required
        >
          <option value="">Select gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Race/Ethnicity *
        </label>
        <select
          name="race_ethnicity"
          value={formData.race_ethnicity}
          onChange={handleChange}
          className="input-field"
          required
        >
          <option value="">Select race/ethnicity</option>
          <option value="group A">Group A</option>
          <option value="group B">Group B</option>
          <option value="group C">Group C</option>
          <option value="group D">Group D</option>
          <option value="group E">Group E</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Parental Level of Education *
        </label>
        <select
          name="parental_level_of_education"
          value={formData.parental_level_of_education}
          onChange={handleChange}
          className="input-field"
          required
        >
          <option value="">Select education level</option>
          <option value="some high school">Some High School</option>
          <option value="high school">High School</option>
          <option value="some college">Some College</option>
          <option value="associate's degree">Associate's Degree</option>
          <option value="bachelor's degree">Bachelor's Degree</option>
          <option value="master's degree">Master's Degree</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Lunch Type *
        </label>
        <select
          name="lunch"
          value={formData.lunch}
          onChange={handleChange}
          className="input-field"
          required
        >
          <option value="">Select lunch type</option>
          <option value="standard">Standard</option>
          <option value="free/reduced">Free/Reduced</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Test Preparation Course *
        </label>
        <select
          name="test_preparation_course"
          value={formData.test_preparation_course}
          onChange={handleChange}
          className="input-field"
          required
        >
          <option value="">Select preparation status</option>
          <option value="none">None</option>
          <option value="completed">Completed</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Reading Score (0-100) *
        </label>
        <input
          type="number"
          name="reading_score"
          value={formData.reading_score}
          onChange={handleChange}
          min="0"
          max="100"
          className="input-field"
          placeholder="Enter reading score"
          required
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Writing Score (0-100) *
        </label>
        <input
          type="number"
          name="writing_score"
          value={formData.writing_score}
          onChange={handleChange}
          min="0"
          max="100"
          className="input-field"
          placeholder="Enter writing score"
          required
        />
      </div>

      <button
        type="submit"
        disabled={loading}
        className="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {loading ? 'Predicting...' : 'Predict Math Score'}
      </button>
    </form>
  )
} 