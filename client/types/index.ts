export interface IUserAuth {
	refreshExpiresIn: number;
	token: string;
	payload: IPayload;
}
export interface IPayload {
	email: string;
	exp: number;
	origIat: number;
}
