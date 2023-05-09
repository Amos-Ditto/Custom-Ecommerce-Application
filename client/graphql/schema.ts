export const GetToken = gql`
	mutation tokenAuth($email: String!, $password: String!) {
		tokenAuth(email: $email, password: $password) {
			refreshExpiresIn
			token
			payload
			refreshToken
		}
	}
`;
