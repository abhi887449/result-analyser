import React from 'react'
import Profile from './Profile'
import Results from './Results'
import Loading from './Loading'

// this component will render after result fetched 
const ResultPage = (props) => {
    const {loading,json,setIsLoading}=props
    if(!loading){
        return (
            <>
            <Profile setIsLoading={setIsLoading} profile={json.results.profile}/>
            <Results results = {json.results.results}/>
            </>
          )
    }
  return (
    <Loading />
  )
}

export default ResultPage
