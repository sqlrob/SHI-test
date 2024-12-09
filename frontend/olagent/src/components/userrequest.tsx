'use client'
import { Fragment, useState } from "react"
import useFetch from "react-fetch-hook"
import { useForm, SubmitHandler } from "react-hook-form"
import createTrigger from "react-use-trigger"
import useTrigger from "react-use-trigger/useTrigger"

// Form data and request to the server
type Inputs = {
    request: string
}

// Response from the server
type Answer = {
    response: string
}

const requestTrigger = createTrigger();

function UserRequest() {
    // State holding question for the server, in the same form posted
    const [question, setQuestion] = useState<Inputs | null>();
    
    // Trigger for sending api request to the server
    const requestTriggerValue = useTrigger(requestTrigger);
    
    // Do the post when the user has clicked submit
    const headers = new Headers();
    headers.append('Content-Type', 'application/json')
    const { isLoading, data, error: apiError } = useFetch<Answer>("http://localhost:8000/api/recommend", { 
        depends: [requestTriggerValue,question], method: "POST", body:JSON.stringify(question), headers  })

    // Form support
    const {
        register,
        handleSubmit,
        formState: { errors }
    } = useForm<Inputs>()
    
    const onSubmit: SubmitHandler<Inputs> = (data) => { setQuestion(data); requestTrigger() }
    return (
        <Fragment>
            <div>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <textarea placeholder="Ask the Librarian a question" {...register("request")} required />
                    {errors.request && <span>You need to ask a question!</span>}
                    {!isLoading ? <button type='submit'>Ask the question</button> : null}
                </form>
            </div>
            <div>{data?.response}</div>
            <div>{apiError ? "Sorry, I can't help you" : null}</div>
        </Fragment>
    )
}

export default UserRequest;