#!/bin/bash
# Script for setup environment variables


export AUTH0_DOMAIN="cemakdag-services.eu.auth0.com"
echo $AUTH0_DOMAIN
export ALGORITHMS="RS256"
echo $ALGORITHMS
export API_AUDIENCE="casting-agency"
echo $API_AUDIENCE
export CLIENT_ID="KXYhatULUX815cOLpIB7F39ckoXrxXKe"
echo $CLIENT_ID
export FLASK_APP=app.py
echo $FLASK_APP
export DATABASE_URL="postgres://spifnvdkxgeahy:4f76e465bd8833b0cf22a18591ec5a58797203cbaf69109b97f8dd21491af44f@ec2-176-34-222-188.eu-west-1.compute.amazonaws.com:5432/dcj5k4g1a0p6hv"
echo $DATABASE_URL
export casting_assistant_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imp4MFlyZmNKajhpdWNKSFh5X3NXYiJ9.eyJpc3MiOiJodHRwczovL2NlbWFrZGFnLXNlcnZpY2VzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDk3Y2YyYTljMzA5NzAwNjk5MTQzOTYiLCJhdWQiOiJjYXN0aW5nLWFnZW5jeSIsImlhdCI6MTYyMTk1NTg4MywiZXhwIjoxNjIyMDQyMjgzLCJhenAiOiJLWFloYXRVTFVYODE1Y09McElCN0YzOWNrb1hyeFhLZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.jH94bKTgicCaeNu14p4qai4Sg5TGvB7jAAE9Z52t_mAdIqV6RSbug0VKIB5LalqWI4paAd1z1Ca0MUxL3cTohyiZVmWFChl6sXogE2IrXebqDr1j3PQmzf02lMCvKP7ResA6T3M2oRVcNyK2FfKFF8HjtiYkWCWv7k_cOqsvNCun72X5yt0aJBuKbScPf2WOLlqLDkzuO5xyNVLfdrstYrbnT_ku3_Dru7CpAwOE3yBt34jcwvt6lJFqs6gmHcEFfhe3gBGy297b5fboJ18dYMxJ6Q49Jcn8QjOEhS_ylZ2voH-l6Rsh3KlENJztk5HufYZcXFJT55zXDbsDUyT2uA"
echo $casting_assistant_token
export casting_director_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imp4MFlyZmNKajhpdWNKSFh5X3NXYiJ9.eyJpc3MiOiJodHRwczovL2NlbWFrZGFnLXNlcnZpY2VzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDlmYWNjZjE0YjM5YTAwNmFhMTQwZjQiLCJhdWQiOiJjYXN0aW5nLWFnZW5jeSIsImlhdCI6MTYyMTk1NTkzOSwiZXhwIjoxNjIyMDQyMzM5LCJhenAiOiJLWFloYXRVTFVYODE1Y09McElCN0YzOWNrb1hyeFhLZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.ZURbruFxP7lgdiq1RojkmuXmjz8yeWbogJ4KKGbM14tMtPNjpmUrVMUAWXP1BqD-ezYZPd7RA3sSutSSJ1pwwHxd7hA5ifqm1YILnKkK7R2kbKmpwg7Ktzlk6rVeb3C-Yrt_XZNP3_mCmC6lD6AKVqbt4ha03bptAnS4Yn4uJ5qpGd5VKEG0ZcaLwQURA6MNfXPiy9nBIMW-7qT_5EkbqajVOLDt9NbIB8HRlmhfyh8g5WRupwZ-K9rlW4P31_rhYZOPJvIRUF2fFRdBGHcsWX-Vm9UJRiG3lwzrqRURayX4Tydm4w_e7HbWHA6az8uCCOr70qD-LvBrHmcC-OKqZw"
echo $casting_director_token
export executive_producer_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imp4MFlyZmNKajhpdWNKSFh5X3NXYiJ9.eyJpc3MiOiJodHRwczovL2NlbWFrZGFnLXNlcnZpY2VzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFiOWVjMGEwYTk3NjAwNzBkOWNmYmMiLCJhdWQiOiJjYXN0aW5nLWFnZW5jeSIsImlhdCI6MTYyMTk1NjAwNiwiZXhwIjoxNjIyMDQyNDA2LCJhenAiOiJLWFloYXRVTFVYODE1Y09McElCN0YzOWNrb1hyeFhLZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.ROvfFO5A9voxitUOTXFPKiPeEVT-RIIa2fNfnwx6zoFAtV0cxjBoAHibE5252DNs5QTORCYVQ54nVM3mXHYMInYfgA73fSVc3RBfPSY9Vun8F_dyMk5BEW8JY7Zl8YgoQmUU2dz8zwFyifpyolinI02siUofuONl5PMS1-pGFS_dVf5rwW1DhtKyAy1EIORV2XLWXSnu1AY0sSLDEiV-4pGUXUeF2b8shTs1Pn7ptiKyEEJUoManHGQvHNt0JSZtPI9FsK8_2L1FsJ5ZuomQs2SD5j7PTHsakabbh5SElumb2S5x4kJDMeQEQ9026_o3cr36nq0L-qjhj7tdwh5RZg"
echo $executive_producer_token