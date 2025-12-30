def analyze_student_performance(student_records):
    strength_threshold = 70
    weakness_threshold = 60
    results = []
    
    for student in student_records:
        strength_count = 0
        weakness_count = 0
        strengths_list = []
        weaknesses_list = []
        total_modules = len(student.get('modules', []))
        
        for module in student.get('modules', []):
            score = module.get('score', 0)
            
            #Before modification - if score >= strength_threshold:
            # AFTER:
            attendance = module.get('attendance', 100)
            if score >= strength_threshold and attendance > 75:
                strength_count += 1
                strengths_list.append(module.get('name', 'Unknown'))
            elif score < weakness_threshold:
                weakness_count += 1
                weaknesses_list.append(module.get('name', 'Unknown'))
        
        if strength_count > weakness_count:
            recommendation = "High Achiever - Continue Current Strategy"
        elif weakness_count > strength_count:
            recommendation = "Requires Intervention - Schedule Academic Support"
        else:
            recommendation = "Balanced Performance - Monitor Progress"
        
        strength_ratio = (strength_count / total_modules * 100) if total_modules > 0 else 0
        
        result = {
            'student_name': student.get('name', 'Unknown'),
            'strength_count': strength_count,
            'weakness_count': weakness_count,
            'strengths': strengths_list,
            'weaknesses': weaknesses_list,
            'recommendation': recommendation,
            'strength_ratio': round(strength_ratio, 2)
        }
        results.append(result)
    
    return results

# Test with your data
test_data = [{
    'name': 'Test Student',
    'modules': [
        {'name': 'Mathematics', 'score': 78},
        {'name': 'Programming', 'score': 72},
        {'name': 'Databases', 'score': 58},
        {'name': 'Statistics', 'score': 45}
    ]
}]

results = analyze_student_performance(test_data)
for r in results:
    print(f"Student: {r['student_name']}")
    print(f"Strengths: {r['strengths']}")
    print(f"Weaknesses: {r['weaknesses']}")
    print(f"Recommendation: {r['recommendation']}")

    print(f"Strength Ratio: {r['strength_ratio']}%")
