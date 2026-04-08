# data/emails.py
EMAILS_DATABASE = [
    # Easy level emails (spam vs not spam)
    {
        'from': 'winner@lottery.com',
        'subject': 'YOU WON $1,000,000!',
        'body': 'Click here to claim your prize!',
        'correct_category': 'spam',
        'difficulty': 'easy',
        'urgency': 'normal',
        'department': 'none'
    },
    {
        'from': 'ceo@company.com',
        'subject': 'Important: Q4 Goals',
        'body': 'Team, please review the quarterly targets.',
        'correct_category': 'not_spam',
        'difficulty': 'easy',
        'urgency': 'normal',
        'department': 'general'
    },
    {
        'from': 'security@bank.com',
        'subject': 'Verify your account now',
        'body': 'Your account will be locked unless you verify.',
        'correct_category': 'spam',
        'difficulty': 'easy',
        'urgency': 'urgent',
        'department': 'none'
    },
    {
        'from': 'manager@company.com',
        'subject': 'Team Meeting Tomorrow',
        'body': 'Please join the team meeting at 10am.',
        'correct_category': 'not_spam',
        'difficulty': 'easy',
        'urgency': 'normal',
        'department': 'general'
    },
    
    # Medium level emails
    {
        'from': 'client@bigcorp.com',
        'subject': 'URGENT: Server Down!',
        'body': 'Our systems are offline, need immediate help!',
        'correct_category': 'urgent',
        'difficulty': 'medium',
        'urgency': 'urgent',
        'department': 'engineering'
    },
    {
        'from': 'customer@email.com',
        'subject': 'Product not working',
        'body': 'I need help with my recent purchase.',
        'correct_category': 'support',
        'difficulty': 'medium',
        'urgency': 'normal',
        'department': 'support'
    },
    {
        'from': 'hr@company.com',
        'subject': 'Payroll Update',
        'body': 'Your salary has been processed.',
        'correct_category': 'normal',
        'difficulty': 'medium',
        'urgency': 'normal',
        'department': 'hr'
    },
    {
        'from': 'boss@company.com',
        'subject': 'Client meeting in 1 hour',
        'body': 'Prepare the presentation ASAP!',
        'correct_category': 'urgent',
        'difficulty': 'medium',
        'urgency': 'urgent',
        'department': 'sales'
    },
    {
        'from': 'newsletter@tech.com',
        'subject': 'Weekly Tech News',
        'body': 'Here are the top stories this week.',
        'correct_category': 'normal',
        'difficulty': 'medium',
        'urgency': 'normal',
        'department': 'general'
    },
    
    # Hard level emails
    {
        'from': 'legal@company.com',
        'subject': 'Contract Review Needed',
        'body': 'Please review the attached contract by EOD.',
        'correct_category': 'urgent',
        'difficulty': 'hard',
        'urgency': 'urgent',
        'department': 'legal'
    },
    {
        'from': 'support@software.com',
        'subject': 'Bug Report #234',
        'body': 'Critical bug affecting all users.',
        'correct_category': 'support',
        'difficulty': 'hard',
        'urgency': 'urgent',
        'department': 'engineering'
    },
    {
        'from': 'partner@vendor.com',
        'subject': 'Invoice Payment Due',
        'body': 'Payment for last month is overdue.',
        'correct_category': 'normal',
        'difficulty': 'hard',
        'urgency': 'urgent',
        'department': 'finance'
    }
]