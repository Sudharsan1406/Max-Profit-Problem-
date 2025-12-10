# Max-Profit-Problem-
# 🚀 Max Profit Optimization System

An interactive Streamlit application that calculates the optimal combination of properties (Theatre, Pub, Commercial Park) to maximize profit within a given time constraint.

## 📌 Project Overview

This project solves a real-estate scheduling problem where different buildings require different construction times and generate earnings per operational time unit.


### You are given:

A total time n

Three building types with different build times and earning rates

Your goal is to find:

How many Theatres, Pubs, and Commercial Parks can be constructed

Without exceeding total time n

While maximizing profit

The system uses a brute-force optimization approach to determine the best combination.

### 🧠 Problem Rules
Building Type	Build Time	Earnings per Operational Unit
🎭 Theatre	5 units	$1500
🍺 Pub	4 units	$1000
🏢 Commercial Park	10 units	$2000

### Additional Constraints

1. Only one building can be constructed at a time.

2. Earnings start only after construction completes.

3. Land availability is infinite (no space constraints).

### 🏗️ How Profit Is Calculated

#### For each building:

Operational Time = n – Build Time
Profit = Count × Operational Time × Earning Rate

#### Example

If n = 9:

Theatre → build 5 → runs for 4 → 4 × 1500 = 6000

Pub → build 4 → runs for 5 → 5 × 1000 = 5000

##### Total Profit = 11,000


### ⚙️ Algorithm Approach

A simple and efficient brute-force search is used.

#### Steps:

1. Loop all possible values of T, P, C

2. Compute total build time → skip if it exceeds n

3. Compute operational times

4. Calculate total profit

5. Track the combination with maximum profit

Brute-force is feasible because construction times (4, 5, 10) are small.

### 🧩 Backend Code (Core Logic)
def max_profit(n):
    T_time, P_time, C_time = 5, 4, 10
    T_rate, P_rate, C_rate = 1500, 1000, 2000

    best_profit = -1
    best_combo = (0, 0, 0)

    for T in range(n // T_time + 1):
        for P in range(n // P_time + 1):
            for C in range(n // C_time + 1):

                time_used = T*T_time + P*P_time + C*C_time
                if time_used > n:
                    continue

                profit = (
                    T * max(0, n - T_time) * T_rate +
                    P * max(0, n - P_time) * P_rate +
                    C * max(0, n - C_time) * C_rate
                )

                if profit > best_profit:
                    best_profit = profit
                    best_combo = (T, P, C)

    return best_profit, best_combo

### 🖥️ Streamlit UI Features

    Clean, light professional interface
    
    Input for total time units
    
    Display of building details
    
    Maximum profit calculation
    
    Optimal combination of T / P / C
    
    Detailed Earnings Breakdown Table
    
    Business rules section


### 📊 Sample Output

#### Input:

n = 9

#### Output:

Theatres: 1
Pubs: 1
Commercial Parks: 0
Total Profit = $11,000


### 👤 Author

#### Sudharsan M S
Max Profit Optimization System — Streamlit Implementation
