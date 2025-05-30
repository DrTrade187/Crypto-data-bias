
import streamlit as st

# Define logic function
def determine_bias(oi, price, vol, fund):
    if oi == "up":
        if price == "up":
            if vol == "up":
                if fund == "pos":
                    return "Bullish, but watch for long crowding"
                elif fund == "neutral":
                    return "Healthy Bullish"
                else:
                    return "Bullish with potential squeeze fuel"
            elif vol == "neutral":
                if fund == "pos":
                    return "Cautious Bullish, volume needs to confirm"
                elif fund == "neutral":
                    return "Cautious Bullish, needs breakout fuel"
                else:
                    return "Hidden strength possible (absorption), watch volume"
            else:
                if fund == "pos":
                    return "Weak rally, vulnerable to reversal"
                elif fund == "neutral":
                    return "Cautious Bullish, lacking conviction"
                else:
                    return "Bullish divergence, squeeze watch"
        elif price == "down":
            if vol == "up":
                if fund == "pos":
                    return "Bearish, longs trapped or being punished"
                elif fund == "neutral":
                    return "Bearish, active sell-side pressure"
                else:
                    return "Bearish, but possible short squeeze setup"
            elif vol == "neutral":
                if fund == "pos":
                    return "Weak longs being drained, bias bearish"
                elif fund == "neutral":
                    return "Cautious Bearish, low conviction trend"
                else:
                    return "Shorts in control, but volume confirmation needed"
            else:
                if fund == "pos":
                    return "Bearish fade, exit longs"
                elif fund == "neutral":
                    return "Exhaustion move, potential bounce"
                else:
                    return "Trap setup brewing, possible squeeze"
        else:
            if vol == "up":
                if fund == "pos":
                    return "Sideways grind, potential breakout if OI builds"
                elif fund == "neutral":
                    return "Consolidation with bullish tilt"
                else:
                    return "Choppy zone, potential for short squeeze"
            elif vol == "neutral":
                if fund == "pos":
                    return "Stagnant market with long bias risk"
                elif fund == "neutral":
                    return "Low conviction range, watch for catalyst"
                else:
                    return "Range bound, bears probing — low liquidity risk"
            else:
                if fund == "pos":
                    return "Apathy from bulls, risky long"
                elif fund == "neutral":
                    return "No interest from either side"
                else:
                    return "Short-dominated lull, watch for surprise move"
    elif oi == "neutral":
        if price == "up":
            if vol == "up":
                return "Potential breakout brewing, but needs OI rise"
            elif vol == "neutral":
                return "Drifting upward, weak conviction"
            else:
                return "Likely fade unless volume returns"
        elif price == "down":
            if vol == "up":
                return "Sell pressure real, OI not confirming"
            elif vol == "neutral":
                return "Slow bleed, lack of conviction"
            else:
                return "No participation, potential exhaustion"
        else:
            if vol == "up":
                return "Coiling, breakout possible"
            elif vol == "neutral":
                return "Range-bound, wait for catalyst"
            else:
                return "Apathy zone, no edge"
    else:
        if price == "up":
            if vol == "up":
                return "Short squeeze or exit pump, not sustainable"
            elif vol == "neutral":
                return "Bearish divergence, rally lacks support"
            else:
                return "Dead cat bounce potential"
        elif price == "down":
            if vol == "up":
                return "Longs exiting, momentum with sellers"
            elif vol == "neutral":
                return "Distribution, downside risk"
            else:
                return "Capitulation phase likely"
        else:
            if vol == "up":
                return "Likely redistribution or bear trap setup"
            elif vol == "neutral":
                return "Chop, with bearish lean"
            else:
                return "Exit activity dominating, avoid entries"

# Streamlit UI
st.title("BTC Bias Cheat Sheet Tool")

oi = st.selectbox("Open Interest", ["up", "neutral", "down"])
price = st.selectbox("Price", ["up", "neutral", "down"])
volume = st.selectbox("Volume", ["up", "neutral", "down"])
funding = st.selectbox("Funding Rate", ["pos", "neutral", "neg"])

bias = determine_bias(oi, price, volume, funding)

st.subheader("Bias Interpretation:")
st.write(bias)
