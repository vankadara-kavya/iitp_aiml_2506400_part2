# Retention Strategy

## Overview

I built an RFM segmentation using order data along with some extra signals like support tickets, return rate, web activity, and loyalty tier. This gave me 6 customer segments. The whole point is that different customers need different treatment. You wouldn't send a "we miss you" email to someone who just bought yesterday.

Overall churn rate is **47%**, so almost half our customers are leaving. But it's not the same everywhere. Champions churn at just 8% while At-Risk customers churn at 80%. So if we target the right group with the right action, we can actually make a difference.

---

## Segment-Level Strategy

### 1. Champions (190 customers, 7.9%) | Churn: 8%

**Who they are:** These are our best customers. They ordered recently (avg 26 days ago), buy frequently (avg 6.4 orders), and spend the most (avg ₹5,012). Basically the dream customer.

**What I'd recommend:**
- Don't give them discounts. They're already buying without any push. Discounts would just eat into our margin for no reason.
- Instead, reward them with early access to new launches, a referral bonus, or a personal thank-you message.
- These are also the best candidates for referral programs since they clearly like the brand.

**Revenue at stake:** ₹952K (190 × ₹5,012). Even stopping 5% more from churning saves about ₹47K.

---

### 2. Loyal Customers (160 customers, 6.7%) | Churn: 26%

**Who they are:** Solid regular buyers (avg 4.5 orders), still active (last order about 48 days ago). Not as big as Champions but they're consistent and reliable.

**What I'd recommend:**
- Get them into the loyalty program if they're not already enrolled.
- Send product recommendations based on what they've bought before.
- Give them a little nudge like "You're 2 orders away from Gold tier!"

**Revenue at stake:** ₹484K. If we can move even 10% of the 26% who would churn, that's about ₹13K saved per cycle.

---

### 3. New Customers (371 customers, 15.5%) | Churn: 19%

**Who they are:** These people ordered recently (avg 20 days ago) but only once or twice. They're brand new and haven't built a habit yet.

**What I'd recommend:**
- The first 60 days are critical. This is when they decide if they're staying or leaving.
- Send a welcome series with product tips, how-to guides, and "what to try next" suggestions.
- Offer a small discount on their second order (not the first, they already bought once).
- Make returns easy. From Part 1, I found that customers with moderate returns (1-30%) actually churn LESS than those with zero returns. Let them try things without worrying.

**Revenue at stake:** ₹331K right now. But if these 371 people become Loyal or Champions over time, the long-term value is huge.

---

### 4. Needs Attention (587 customers, 24.5%) | Churn: 46%

**Who they are:** These customers are **unhappy**. They have 2+ support complaints or return more than 30% of what they buy. The interesting thing is their RFM actually looks decent (avg ₹3,738 spending). So they WANT to buy from us, something is just going wrong.

**What I'd recommend:**
- Fix the problem first, sell later. Go through their open tickets and actually resolve them.
- For the high returners, reach out and ask what went wrong. Wrong shade? Wrong size? Damaged in shipping?
- Offer a replacement or store credit, not a discount. Discounts don't fix a bad experience.
- If we resolve their issues, many of these could move to Loyal or Champions since they already spend a lot.

**Revenue at stake:** ₹2.2M total in this segment. These are high-spending customers having a bad time. Fixing their issues has the best ROI of any segment.

---

### 5. Dormant (641 customers, 26.7%) | Churn: 58%

**Who they are:** Low on everything. They only ordered about 1.7 times, spent ₹1,230, and their last order was 106 days ago. They're quietly drifting away.

**What I'd recommend:**
- Only low-cost reactivation. Don't spend heavily on people who were never that engaged in the first place.
- Send a "We miss you" email with a small offer like ₹100 off or free shipping.
- If they don't respond after 2 attempts, move on and focus the budget elsewhere.

**Revenue at stake:** ₹788K total, but with 58% churn and low individual value, the recovery rate will be low. Keep the spending minimal here.

---

### 6. At-Risk (451 customers, 18.8%) | Churn: 80%

**Who they are:** These used to be good customers. They ordered 3-4 times and spent ₹3,022 on average. But they haven't ordered in about 167 days. They're almost gone.

**What I'd recommend:**
- This is an urgent win-back situation. Last chance before they leave for good.
- Personal outreach: "We noticed you haven't ordered in a while. Is everything okay?"
- Give them a real incentive, like 20-25% discount or a free product sample.
- Make it time-limited: "This offer expires in 7 days" creates urgency.
- If they still don't respond, accept the loss and put the budget somewhere else.

**Revenue at stake:** ₹1.36M. Even recovering 15-20% saves ₹200-270K.

---

## Campaign Budget Allocation

If I had ₹100K to spend on retention, here's how I'd split it:

| Priority | Segment | Budget | % | Why |
|----------|---------|--------|---|-----|
| 1 | Needs Attention | ₹30,000 | 30% | Best ROI. Big spenders with fixable problems. Resolving issues costs less than finding new customers. |
| 2 | At-Risk | ₹25,000 | 25% | Urgent. 80% will churn without help. They already have purchase history so winning them back is cheaper than new acquisition. |
| 3 | New Customers | ₹20,000 | 20% | Investment in the future. Converting these 371 people into loyal buyers pays off for years. |
| 4 | Loyal Customers | ₹15,000 | 15% | Protecting what's working. Small spend to keep them engaged before they become At-Risk. |
| 5 | Champions | ₹8,000 | 8% | They're already happy, minimal spend needed. Mostly recognition, not discounts. |
| 6 | Dormant | ₹2,000 | 2% | Lowest ROI. Were never very engaged + 58% churn = poor return. Basic email campaigns only. |

**Why Needs Attention gets the most:** They spend ₹3,738 on average, second only to Champions. Their problem isn't that they don't like us, it's that something went wrong. A ₹500 fix (replacement, credit, apology) on a customer worth ₹3,738 is a 7x return.

**Why Dormant gets the least:** They were never really into the brand (avg 1.7 orders, ₹1,230 total). The cost to reactivate them might be more than they'd ever spend.

---

## Key Takeaway

The main thing I learned from this segmentation is that **churn is not one problem, it's six different problems.** A Champion who leaves is completely different from a Dormant customer who leaves. The Champion probably had one bad experience. The Dormant customer probably never connected with the brand in the first place. Treating everyone the same wastes money and misses the actual issue.
