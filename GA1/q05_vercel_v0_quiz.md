# GA1 — Q5: Deploy a quiz app using Vercel v0

## Problem Summary

The task required creating and deploying a quiz app using Vercel v0 such that the quiz questions are present in the HTML of the home page (not dynamically rendered via JavaScript), and submitting the deployed Vercel URL.

## Requirements

- Use Vercel v0 to create and deploy the quiz app
- Include the question:

  **Which Indian state is famous for tea gardens like Kaziranga?**  
  1. Assam  
  2. Punjab  
  3. Kerala  
  4. Gujarat  
  5. Bihar  

- Ensure questions are present in the page source / HTML of the home page
- Deploy to Vercel and provide the deployed URL

## Issues Encountered

- React warning/error: radio inputs used `checked` without `onChange` (controlled input issue).

## Strategy

- Use v0 to generate a Next.js quiz app with hardcoded question markup (no `map()` rendering from an array).
- Fix the controlled radio inputs by adding explicit `onChange` handlers.
- Publish the app via v0 “Publish to Production” to deploy on Vercel.
- Verify deployed URL works.

## Deployed App URL

https://v0-quiz-web-app-eta-lemon.vercel.app

## Result

PASS
