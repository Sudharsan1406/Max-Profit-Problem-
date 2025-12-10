import streamlit as st

# --------------------------------------------------------
# BACKEND LOGIC (CORRECT VERSION)
# --------------------------------------------------------
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


# --------------------------------------------------------
# STREAMLIT UI (LIGHT THEME)
# --------------------------------------------------------

st.set_page_config(page_title="Max Profit Calculator", layout="wide")

st.title("Max Profit Problem")
st.write("Find the optimal mix of properties to maximize earnings.")

st.header("Available Properties")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🎭 Theatre")
    st.write("• Build Time: **5 units**")
    st.write("• Earnings per Unit Time: **$1500**")
    st.write("• Efficiency: **$300/time**")

with col2:
    st.subheader("🍺 Pub")
    st.write("• Build Time: **4 units**")
    st.write("• Earnings per Unit Time: **$1000**")
    st.write("• Efficiency: **$250/time**")

with col3:
    st.subheader("🏢 Commercial Park")
    st.write("• Build Time: **10 units**")
    st.write("• Earnings per Unit Time: **$2000**")
    st.write("• Efficiency: **$200/time**")

st.markdown("---")

st.header("Time Input")
time_units = st.number_input("Enter Total Time Units (n):", min_value=1, max_value=500, value=9)

if st.button("Calculate Maximum Profit"):
    profit, (T, P, C) = max_profit(time_units)

    st.success(f"Maximum Profit for {time_units} units = **${profit:,}**")

    st.subheader("Optimal Solution")
    colA, colB, colC = st.columns(3)
    colA.metric("Theatres", T)
    colB.metric("Pubs", P)
    colC.metric("Commercial Parks", C)

    # -----------------------------
    # Earnings Breakdown Table
    # -----------------------------
    st.subheader("Earnings Breakdown")

    # Calculate operational times and total per building
    op_T = max(0, time_units - 5) if T > 0 else 0
    op_P = max(0, time_units - 4) if P > 0 else 0
    op_C = max(0, time_units - 10) if C > 0 else 0

    data = []

    if T > 0:
        data.append([
            "Theatre", T, "5", op_T, "$1500", f"${T * op_T * 1500:,}"
        ])

    if P > 0:
        data.append([
            "Pub", P, "4", op_P, "$1000", f"${P * op_P * 1000:,}"
        ])

    if C > 0:
        data.append([
            "Commercial Park", C, "10", op_C, "$2000", f"${C * op_C * 2000:,}"
        ])

    st.table(
        {
            "Building": [row[0] for row in data],
            "Count": [row[1] for row in data],
            "Build Time": [row[2] for row in data],
            "Operates For": [row[3] for row in data],
            "Rate": [row[4] for row in data],
            "Total": [row[5] for row in data],
        }
    )

